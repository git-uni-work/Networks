# " TCP SERVER "

The goal of the task is to create a multi-threaded server for TCP / IP communication and implement the communication protocol according to the given specification. Attention, the implementation of the client part is not part of the task! The client part is implemented by a test environment.

The server does not have to be really multi-threaded, it just has to manage to serve several clients at once. It doesn't matter if you achieve this in one thread or with the help of processes, especially if you pass all the tests.

Create a server for automatic control of remote robots. The robots log in to the server themselves and the server guides them to the center of the coordinate system. For testing purposes, each robot starts at random coordinates and tries to reach the coordinate [0,0]. The robot must pick up the secret at the target coordinate. On the way to the goal, the robots may encounter obstacles that they must bypass. The server manages to navigate multiple robots at once and implements a communication protocol without errors.

Communication between the server and the robots is realized by a full text protocol. Each command ends with a pair of special symbols "\\ a \\ b". (These are the **two** characters '\\ a' and '\\ b'.) The server must follow the communication protocol in detail exactly, but must take into account imperfect robot firmware (see the Special Situations section).

Each robot starts communication by sending its username (message CLIENT\_USERNAME). The user name can be any sequence of 18 characters that does not contain the sequence "\\ a \\ b". In the next step, the client server prompts you to send a Key ID (SERVER\_KEY\_REQUEST message), which is actually the identifier of the key pair it wants to use for authentication. The client responds with a CLIENT\_KEY\_ID message in which it sends a Key ID. After that, the server knows the correct key pair, so it can compute the "hash" code from the username according to the following formula:

    Username: Mnau!

    ASCII Representation: 77 110 97 117 33

    Resulting hash: ((77 + 110 + 97 + 117 + 33) * 1000)% 65536 = 40784

The resulting hash is a 16-bit number in decimal. The server then adds the server key to the hash so that if the 16-bit capacity is exceeded, the value simply overflows:

    (40784 + 54621)% 65536 = 29869

The resulting server confirmation code is sent as text to the client in the SERVER\_CONFIRM message. The client calculates a hash back from the received code and compares it with the expected hash, which it calculated from the username. If they match, it creates a client confirmation code. The calculation of the client confirmation code is similar to the server, only the client key is used:

    (40784 + 45328)% 65536 = 20576

The client confirmation code is sent to the server in a CLIENT\_CONFIRMATION message, which calculates a hash back from it and compares it to the original username hash. If both values ​​match, it sends a SERVER\_OK message, otherwise it responds with a SERVER\_LOGIN\_FAILED message and closes the connection. The whole sequence is in the following picture:

    Client Server
    ------------------------------------------
    CLIENT_USERNAME --->
                        <--- SERVER_KEY_REQUEST
    CLIENT_KEY_ID --->
                        <--- SERVER_CONFIRMATION
    CLIENT_CONFIRMATION --->
                        <--- SERVER_OK
                                  or
                                SERVER_LOGIN_FAILED
                          .
                          .
                          .

The server does not know the usernames in advance. Therefore, robots can choose any name, but they must know the set of client and server keys. The key pair ensures two-way authentication while preventing the authentication process from being compromised by simply eavesdropping on the communication.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_pohyb-robota-k-c%C3%ADli)Move the robot to the target

The robot can only move straight (SERVER\_MOVE) and is able to rotate in place to the right (SERVER\_TURN\_RIGHT) and left (SERVER\_TURN\_LEFT). After each move command, it sends an acknowledgment (CLIENT\_OK), which also includes the current coordinates. The position of the robot is not known to the server at the beginning of the communication. The server must find out the position of the robot (position and direction) only from its answers. To prevent the robot from endlessly wandering in space, each robot has a limited number of movements (only moving forward). The number of movements should be sufficient to reasonably move the robot to the target. The following is a demonstration of communication. The server first moves the robot forward twice to detect its current state and then guides it towards the target coordinate [0,0].

    Client Server
    ------------------------------------------
                      .
                      .
                      .
                    <--- SERVER_MOVE
                              or
                            SERVER_TURN_LEFT
                              or
                            SERVER_TURN_RIGHT
    CLIENT_OK --->
                    <--- SERVER_MOVE
                              or
                            SERVER_TURN_LEFT
                              or
                            SERVER_TURN_RIGHT
    CLIENT_OK --->
                    <--- SERVER_MOVE
                              or
                            SERVER_TURN_LEFT
                              or
                            SERVER_TURN_RIGHT
                      .
                      .
                      .

Immediately after authentication, the robot expects at least one movement command - SERVER\_MOVE, SERVER\_TURN\_LEFT or SERVER\_TURN\_RIGHT! You can't just try to pick up a secret. There are many obstacles on the way to the goal, which the robots have to overcome by detour. The following rules apply to obstacles:

-   An obstacle always occupies a single coordinate.
-   It is guaranteed that each obstacle has empty all adjacent coordinates (so you can always easily get around).
-   It is guaranteed that the obstacle never occupies the coordinate [0,0].

The obstacle is detected when the robot is instructed to move forward (SERVER\_MOVE), but the coordinates do not change (the CLIENT\_OK message contains the same coordinates as in the previous step). If the movement is not performed, it will not be deducted from the number of remaining steps of the robot.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_vyzvednut%C3%AD-tajn%C3%A9ho-vzkazu)Picking up a secret message

After the robot reaches the target coordinate [0,0], it tries to pick up a secret message (SERVER\_PICK\_UP message). If the robot is asked to retrieve the message and is not at the target coordinate, the robot's self-destruction starts and communication with the server is interrupted. The robot responds with a CLIENT\_MESSAGE message when trying to retrieve the target coordinate. The server must respond to this message with a SERVER\_LOGOUT message. (It is guaranteed that a secret message will never match a CLIENT\_RECHARGING message if this message is received by the server after a pickup request. It is always a recharge.) Then both the client and the server terminate the connection. Example of searching the target area:

    Client Server
    ------------------------------------------
                      .
                      .
                      .
                    <--- SERVER_PICK_UP
    CLIENT_MESSAGE --->
                    <--- SERVER_LOGOUT

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_dob%C3%ADjen%C3%AD)Charging

Each of the robots has a limited energy source. If it starts to run out of batteries, it notifies the server and then starts charging itself from the solar panel. It does not respond to any messages during charging. When finished, it informs the server and continues to operate where it left off before recharging. If the robot does not end charging within the TIMEOUT\_RECHARGING interval, the server terminates the connection.

    Client Server
    ------------------------------------------
    CLIENT_USERNAME --->
                      <--- SERVER_CONFIRMATION
    CLIENT_RECHARGING --->

          ...

    CLIENT_FULL_POWER --->
    CLIENT_OK --->
                      <--- SERVER_OK
                                or
                              SERVER_LOGIN_FAILED
                        .
                        .
                        .

Another example:

    Client Server
    ------------------------------------------
                        .
                        .
                        .
                      <--- SERVER_MOVE
    CLIENT_OK --->
    CLIENT_RECHARGING --->

          ...

    CLIENT_FULL_POWER --->
                      <--- SERVER_MOVE
    CLIENT_OK --->
                      .
                      .
                      .


Error situations
------------------------------------------------------------------------------------------------

Some robots may have corrupted firmware and may communicate poorly. The server should detect this inappropriate behavior and respond properly.

### Authentication errors

If the CLIENT\_KEY\_ID message contains a Key ID that is out of the expected range (that is, a number that is not between 0-4), the server responds with a SERVER\_KEY\_OUT\_OF\_RANGE\_ERROR error message and closes the connection. Negative values ​​are also considered a number for simplicity. If there is no number (eg letters) in the CLIENT\_KEY\_ID message, the server responds with a SERVER\_SYNTAX\_ERROR error.

If the CLIENT\_CONFIRMATION message contains a numeric value (even a negative number) that does not match the expected acknowledgment, the server sends a SERVER\_LOGIN\_FAILED message and closes the connection. If it is not a purely numeric value at all, the server sends a SERVER\_SYNTAX\_ERROR message and closes the connection.

### Syntax error

The server always responds to a syntax error immediately after receiving the message in which it detected the error. The server sends a SERVER\_SYNTAX\_ERROR message to the robot and then it must end the connection as soon as possible. Syntactically incorrect messages:

-   The incoming message is longer than the number of characters defined for each message (including the trailing \\ and \\ b characters). Message lengths are defined in the table with an overview of messages from the client.
-   The incoming message does not parse any of the CLIENT\_USERNAME, CLIENT\_KEY\_ID, CLIENT\_CONFIRMATION, CLIENT\_OK, CLIENT\_RECHARGING, and CLIENT\_FULL\_POWER messages.

Each incoming message is tested for maximum size, and only CLIENT\_CONFIRMATION, CLIENT\_OK, CLIENT\_RECHARGING, and CLIENT\_FULL\_POWER messages are tested for their content (CLIENT\_USERNAME and CLIENT\_MESSAGE messages can contain anything).

### Logic error

The logic error only occurs during charging - when the robot sends the charging info (CLIENT\_RECHARGING) and then sends any message other than CLIENT\_FULL\_POWER or when it sends a CLIENT\_FULL\_POWER message, without first sending CLIENT\_RECHARGING. The server responds to such situations by sending a SERVER\_LOGIC\_ERROR message and terminating the connection immediately.

### Timeout

The protocol for communication with robots contains two types of timeout:

-   TIMEOUT - timeout for communication. If the robot or server does not receive any communication from its counterpart (but it does not have to be the whole message) during this time interval, they consider the connection lost and terminate it immediately.
-   TIMEOUT\_RECHARGING - timeout for robot charging. After the server receives the CLIENT\_RECHARGING message, the robot must send a CLIENT\_FULL\_POWER message no later than this time interval. If the robot fails to do so, the server must end the connection immediately.

Special situations
---------------------------------------------------------------------------------------------------------

When communicating over a more complicated network infrastructure, two situations can occur:

-   The message can arrive divided into several parts, which are read from the socket sequentially. (This is due to segmentation and possible delays of some segments in the network path.)
-   Messages sent in quick succession can arrive almost simultaneously. In one read from the socket, both can be read at once. (This happens if the server fails to retrieve the first message from the buffer before the second message arrives.)

Using a direct connection between the server and the robots in combination with powerful hardware, these situations cannot occur naturally, so they are created artificially by the tester. In some tests, both situations are combined.

Every properly implemented server should be able to cope with this situation. Robot companies take this fact into account and even like to abuse it. If there is a situation in the log where messages from the robot have a predefined order, they are sent in this order at once. This allows the probes to reduce their consumption and simplifies the implementation of the protocol (from their point of view).

Server optimization
---------------------------------------------------------------------------------------------------

The server optimizes the protocol so that it does not wait for the completion of a message that is obviously bad. For example, when prompted for authentication, the robot sends only part of the message with the user name. For example, the server receives 22 user name characters, but still does not receive the \\ a \\ b termination sequence. Since the maximum message length is 20 characters, it is clear that the received message cannot be valid. Therefore, the server responds by not waiting for the rest of the message, but sends a SERVER\_SYNTAX\_ERROR message and closes the connection. In principle, he should do the same when retrieving a secret message.

In the case of the part of the communication in which the robot navigates to the target coordinates, it expects three possible messages: CLIENT\_OK, CLIENT\_RECHARGING or CLIENT\_FULL\_POWER. If the server retrieves part of the incomplete message and this part is longer than the maximum length of these messages, it sends SERVER\_SYNTAX\_ERROR and closes the connection. To help with optimization, the maximum size of each message is listed in the table.

Communication example
-------------------------------------------------------------------------------------------------------

    C: "Oompa Loompa \ a \ b"
    S: "107 KEY REQUEST \ a \ b"
    C: "0 \ a \ b"
    S: "64907 \ a \ b"
    C: "8389 \ a \ b"
    S: "200 OK \ a \ b"
    S: "102 MOVE \ a \ b"
    C: "OK 0 0 \ a \ b"
    S: "102 MOVE \ a \ b"
    C: "OK -1 0 \ a \ b"
    S: "104 TURN RIGHT \ a \ b"
    C: "OK -1 0 \ a \ b"
    S: "104 TURN RIGHT \ a \ b"
    C: "OK -1 0 \ a \ b"
    S: "102 MOVE \ a \ b"
    C: "OK 0 0 \ a \ b"
    S: "105 GET MESSAGE \ a \ b"
    C: "Secret message. \ A \ b"
    S: "106 LOGOUT \ a \ b"

Testing
--------------------------------------------------------------------------------------

An image of the Tiny Core Linux operating system is ready for testing, which includes a homework tester. The image is compatible with VirtualBox.

### Tester

Download and unzip the image. Run the resulting file in VirtualBox. The shell is immediately available upon startup and boot. The tester is started with the *tester* command :

    tester <port number> <remote address> [test numbers]

The first parameter is the port number on which your server will listen. The parameter with the remote server address follows. If your server is running on the same computer as VirtualBox, use the default gateway address

The output is relatively long, so it is advantageous to redirect it to the *less* command , in which you can move well.

If no test number is entered, all tests run sequentially. Tests can also be run individually. The following example runs tests 2, 3, and 8:

    tester 3999 10.0.2.2 2 3 8 | less

#### Possible problems in the windows operating system

In some Windows installations, there is a problem with the standard virtual machine configuration. If the virtual tester cannot connect to the server under test on the host operating system, use the following procedure:

-   With the tester virtual machine turned off, change the network adapter settings from NAT to Host-only network.
-   The network interface belonging to VirtualBox should appear in the host OS. This can be found from the command line with the *ipconfig* command . The IP address of this interface will probably be 192.168.56.1/24.
-   In the virtual tester, it is now necessary to manually set the IP address of the eth0 network interface:

sudo ifconfig eth0 192.168.56.2 netmask 255.255.255.0

-   It is now possible to run the tester, but enter the IP address of the network interface in the host OS as the destination address:

tester 3999 192.168.56.1

### Download

VirtualBox application: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

Tester: [All versions of the tester for download](https://drive.google.com/drive/folders/1QzPyzZeLNWZhjtbaTGehyNu-zgHcInta?usp=sharing)

The directory from the previous link contains directories with development versions of the tester. You will find the following files in each directory labeled vX (where *X* is the version number):

-   BI-PSI\_tester\_2021\_vX.ova - virtual with tester
-   psi-tester-2021-vX\_x64.bz2 - version for linux 64-bit
-   psi-tester-2021-vX\_x86.bz2 - version for linux 32-bit
