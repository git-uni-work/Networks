-   User logged in [samymbas](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#)
    -   Log out
-   Log in

[FIT CTU Course Pages](https://courses.fit.cvut.cz/)

BI-PSI Computer Networking-

-   [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#)
     Past semesters
    -   [B101](https://courses.fit.cvut.cz/BI-PSI/@B101/)
    -   [B102](https://courses.fit.cvut.cz/BI-PSI/@B102/)
    -   [B111](https://courses.fit.cvut.cz/BI-PSI/@B111/)
    -   [B112](https://courses.fit.cvut.cz/BI-PSI/@B112/)
    -   [B122](https://courses.fit.cvut.cz/BI-PSI/@B122/)
    -   [B131](https://courses.fit.cvut.cz/BI-PSI/@B131/)
    -   [B132](https://courses.fit.cvut.cz/BI-PSI/@B132/)
    -   [B141](https://courses.fit.cvut.cz/BI-PSI/@B141/)
    -   [B142](https://courses.fit.cvut.cz/BI-PSI/@B142/)
    -   [B151](https://courses.fit.cvut.cz/BI-PSI/@B151/)
    -   [B152](https://courses.fit.cvut.cz/BI-PSI/@B152/)
    -   [B161](https://courses.fit.cvut.cz/BI-PSI/@B161/)
    -   [B162](https://courses.fit.cvut.cz/BI-PSI/@B162/)
    -   [B171](https://courses.fit.cvut.cz/BI-PSI/@B171/)
    -   [B172](https://courses.fit.cvut.cz/BI-PSI/@B172/)
    -   [B182](https://courses.fit.cvut.cz/BI-PSI/@B182/)
    -   [B192](https://courses.fit.cvut.cz/BI-PSI/@B192/)
    -   [B202](https://courses.fit.cvut.cz/BI-PSI/@B202/)
    -   [master](https://courses.fit.cvut.cz/BI-PSI/)
-   [](https://gitlab.fit.cvut.cz/BI-PSI/bi-psi/blob/master/homework/index.adoc)
     View on GitLab
-   [](https://gitlab.fit.cvut.cz/BI-PSI/bi-psi/issues/new?issue[title]=homework/index.adoc:%20)
     Report an error

[Jdi na navigaci předmětu](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#nav)

Homework
========

Content
-------

1.  [Annotation](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_anotace)
2.  [Assignment](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_zad%C3%A1n%C3%AD)
3.  [Detailed specifications](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_detailn%C3%AD-specifikace)
    1.  [Authentication](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_autentizace)
    2.  [Move the robot to the target](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_pohyb-robota-k-c%C3%ADli)
    3.  [Picking up a secret message](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_vyzvednut%C3%AD-tajn%C3%A9ho-vzkazu)
    4.  [Charging](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_dob%C3%ADjen%C3%AD)

4.  [Error situations](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_chybov%C3%A9-situace)
    1.  [Authentication errors](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_chyby-p%C5%99i-autentizaci)
    2.  [Syntax error](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_syntaktick%C3%A1-chyba)
    3.  [Logic error](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_logick%C3%A1-chyba)
    4.  [Timeout](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_timeout)

5.  [Special situations](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_speci%C3%A1ln%C3%AD-situace)
6.  [Server optimization](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_optimalizace-serveru)
7.  [Communication example](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_uk%C3%A1zka-komunikace)
8.  [Testing](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_testov%C3%A1n%C3%AD)
    1.  [Tester](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_tester)
    2.  [Download](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_ke-sta%C5%BEen%C3%AD)

9.  [Solution requirements](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_po%C5%BEadavky-na-%C5%99e%C5%A1en%C3%AD)
10. [Submission](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_odevzd%C3%A1n%C3%AD)
    1.  [Upload to archive server](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_n%C3%A1hr%C3%A1n%C3%AD-na-archiva%C4%8Dn%C3%AD-server)
    2.  [Personal presentation](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_osobn%C3%AD-prezentace)

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_anotace)Annotation
-----------------------------------------------------------------------------

The goal of the task is to create a multi-threaded server for TCP / IP communication and implement the communication protocol according to the given specification. Attention, the implementation of the client part is not part of the task! The client part is implemented by a test environment.

###### Poznámka:

The server does not have to be really multi-threaded, it just has to manage to serve several clients at once. It doesn't matter if you achieve this in one thread or with the help of processes, especially if you pass all the tests.

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_zad%C3%A1n%C3%AD)Assignment
--------------------------------------------------------------------------------------

Create a server for automatic control of remote robots. The robots log in to the server themselves and the server guides them to the center of the coordinate system. For testing purposes, each robot starts at random coordinates and tries to reach the coordinate [0,0]. The robot must pick up the secret at the target coordinate. On the way to the goal, the robots may encounter obstacles that they must bypass. The server manages to navigate multiple robots at once and implements a communication protocol without errors.

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_detailn%C3%AD-specifikace)Detailed specifications
------------------------------------------------------------------------------------------------------------

Communication between the server and the robots is realized by a full text protocol. Each command ends with a pair of special symbols "\\ a \\ b". (These are the **two** characters '\\ a' and '\\ b'.) The server must follow the communication protocol in detail exactly, but must take into account imperfect robot firmware (see the Special Situations section).

Server messages:

Name

Message

Description

SERVER\_CONFIRMATION

\<16-bit number in decimal notation\> \\ a \\ b

Message with confirmation code. It can contain a maximum of 5 numbers and the ending sequence \\ a \\ b.

SERVER\_MOVE

102 MOVE \\ a \\ b

Command to move one field forward

SERVER\_TURN\_LEFT

103 TURN LEFT \\ a \\ b

Turn left command

SERVER\_TURN\_RIGHT

104 TURN RIGHT \\ a \\ b

Command to turn right

SERVER\_PICK\_UP

105 GET MESSAGE \\ a \\ b

Message retrieval command

SERVER\_LOGOUT

106 LOGOUT \\ a \\ b

Command to end the connection after successful retrieval of the message

SERVER\_KEY\_REQUEST

107 KEY REQUEST \\ a \\ b

Server request Key ID for communication

SERVER\_OK

200 OK \\ a \\ b

Positive confirmation

SERVER\_LOGIN\_FAILED

300 LOGIN FAILED \\ a \\ b

Failed authentication

SERVER\_SYNTAX\_ERROR

301 SYNTAX ERROR \\ a \\ b

Bad message syntax

SERVER\_LOGIC\_ERROR

302 LOGIC ERROR \\ a \\ b

Message sent in bad situation

SERVER\_KEY\_OUT\_OF\_RANGE\_ERROR

303 KEY OUT OF RANGE \\ a \\ b

Key ID is out of range

Client messages:

Name

Message

Description

Sample

Maximum length

CLIENT\_USERNAME

\<user name\> \\ a \\ b

Message with username. The name can be any sequence of characters except the \\ a \\ b pair.

Umpa\_Lumpa \\ a \\ b

20

CLIENT\_KEY\_ID

\<Key ID\> \\ a \\ b

A message containing a Key ID. It can only contain an integer with a maximum of three digits.

2 \\ a \\ b

5

CLIENT\_CONFIRMATION

\<16-bit number in decimal notation\> \\ a \\ b

Message with confirmation code. It can contain a maximum of 5 numbers and the ending sequence \\ a \\ b.

1009 \\ a \\ b

7

CLIENT\_OK

OK \<x\> \<y\> \\ a \\ b

Confirmation of the execution of the movement, where *x* and *y* are the coordinates of the robot after the execution of the movement command.

OK -3 -1 \\ a \\ b

12

CLIENT\_RECHARGING

RECHARGING \\ a \\ b

The robot began to charge and stopped responding to messages.

12

CLIENT\_FULL\_POWER

FULL POWER \\ a \\ b

The robot has replenished energy and is receiving commands again.

12

CLIENT\_MESSAGE

\<text\> \\ a \\ b

The text of the collected secret message. It can contain any characters except the ending sequence \\ a \\ b.

Haf! \\ A \\ b

100

Time constants:

Name

Value [s]

Description

TIMEOUT

1

Both the server and the client expect a response from the counterparty for this interval.

TIMEOUT\_RECHARGING

5

The time interval during which the robot must complete charging.

Communication with robots can be divided into several phases:

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_autentizace)Authentication

Both the server and the client know five pairs of authentication keys (these are not public and private keys):

Key ID

Server Key

Client Key

0

23019

32037

1

32037

29295

2

18789

13603

3

16443

29533

4

18189

21952

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

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_chybov%C3%A9-situace)Error situations
------------------------------------------------------------------------------------------------

Some robots may have corrupted firmware and may communicate poorly. The server should detect this inappropriate behavior and respond properly.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_chyby-p%C5%99i-autentizaci)Authentication errors

If the CLIENT\_KEY\_ID message contains a Key ID that is out of the expected range (that is, a number that is not between 0-4), the server responds with a SERVER\_KEY\_OUT\_OF\_RANGE\_ERROR error message and closes the connection. Negative values ​​are also considered a number for simplicity. If there is no number (eg letters) in the CLIENT\_KEY\_ID message, the server responds with a SERVER\_SYNTAX\_ERROR error.

If the CLIENT\_CONFIRMATION message contains a numeric value (even a negative number) that does not match the expected acknowledgment, the server sends a SERVER\_LOGIN\_FAILED message and closes the connection. If it is not a purely numeric value at all, the server sends a SERVER\_SYNTAX\_ERROR message and closes the connection.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_syntaktick%C3%A1-chyba)Syntax error

The server always responds to a syntax error immediately after receiving the message in which it detected the error. The server sends a SERVER\_SYNTAX\_ERROR message to the robot and then it must end the connection as soon as possible. Syntactically incorrect messages:

-   The incoming message is longer than the number of characters defined for each message (including the trailing \\ and \\ b characters). Message lengths are defined in the table with an overview of messages from the client.
-   The incoming message does not parse any of the CLIENT\_USERNAME, CLIENT\_KEY\_ID, CLIENT\_CONFIRMATION, CLIENT\_OK, CLIENT\_RECHARGING, and CLIENT\_FULL\_POWER messages.

Each incoming message is tested for maximum size, and only CLIENT\_CONFIRMATION, CLIENT\_OK, CLIENT\_RECHARGING, and CLIENT\_FULL\_POWER messages are tested for their content (CLIENT\_USERNAME and CLIENT\_MESSAGE messages can contain anything).

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_logick%C3%A1-chyba)Logic error

The logic error only occurs during charging - when the robot sends the charging info (CLIENT\_RECHARGING) and then sends any message other than CLIENT\_FULL\_POWER or when it sends a CLIENT\_FULL\_POWER message, without first sending CLIENT\_RECHARGING. The server responds to such situations by sending a SERVER\_LOGIC\_ERROR message and terminating the connection immediately.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_timeout)Timeout

The protocol for communication with robots contains two types of timeout:

-   TIMEOUT - timeout for communication. If the robot or server does not receive any communication from its counterpart (but it does not have to be the whole message) during this time interval, they consider the connection lost and terminate it immediately.
-   TIMEOUT\_RECHARGING - timeout for robot charging. After the server receives the CLIENT\_RECHARGING message, the robot must send a CLIENT\_FULL\_POWER message no later than this time interval. If the robot fails to do so, the server must end the connection immediately.

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_speci%C3%A1ln%C3%AD-situace)Special situations
---------------------------------------------------------------------------------------------------------

When communicating over a more complicated network infrastructure, two situations can occur:

-   The message can arrive divided into several parts, which are read from the socket sequentially. (This is due to segmentation and possible delays of some segments in the network path.)
-   Messages sent in quick succession can arrive almost simultaneously. In one read from the socket, both can be read at once. (This happens if the server fails to retrieve the first message from the buffer before the second message arrives.)

Using a direct connection between the server and the robots in combination with powerful hardware, these situations cannot occur naturally, so they are created artificially by the tester. In some tests, both situations are combined.

Every properly implemented server should be able to cope with this situation. Robot companies take this fact into account and even like to abuse it. If there is a situation in the log where messages from the robot have a predefined order, they are sent in this order at once. This allows the probes to reduce their consumption and simplifies the implementation of the protocol (from their point of view).

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_optimalizace-serveru)Server optimization
---------------------------------------------------------------------------------------------------

The server optimizes the protocol so that it does not wait for the completion of a message that is obviously bad. For example, when prompted for authentication, the robot sends only part of the message with the user name. For example, the server receives 22 user name characters, but still does not receive the \\ a \\ b termination sequence. Since the maximum message length is 20 characters, it is clear that the received message cannot be valid. Therefore, the server responds by not waiting for the rest of the message, but sends a SERVER\_SYNTAX\_ERROR message and closes the connection. In principle, he should do the same when retrieving a secret message.

In the case of the part of the communication in which the robot navigates to the target coordinates, it expects three possible messages: CLIENT\_OK, CLIENT\_RECHARGING or CLIENT\_FULL\_POWER. If the server retrieves part of the incomplete message and this part is longer than the maximum length of these messages, it sends SERVER\_SYNTAX\_ERROR and closes the connection. To help with optimization, the maximum size of each message is listed in the table.

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_uk%C3%A1zka-komunikace)Communication example
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

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_testov%C3%A1n%C3%AD)Testing
--------------------------------------------------------------------------------------

An image of the Tiny Core Linux operating system is ready for testing, which includes a homework tester. The image is compatible with VirtualBox.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_tester)Tester

Download and unzip the image. Run the resulting file in VirtualBox. The shell is immediately available upon startup and boot. The tester is started with the *tester* command :

    tester <port number> <remote address> [test numbers]

The first parameter is the port number on which your server will listen. The parameter with the remote server address follows. If your server is running on the same computer as VirtualBox, use the default gateway address. The procedure is indicated in the following figure:

![testing image example](./TCP_files/testing-image-example.png)

The output is relatively long, so it is advantageous to redirect it to the *less* command , in which you can move well.

If no test number is entered, all tests run sequentially. Tests can also be run individually. The following example runs tests 2, 3, and 8:

    tester 3999 10.0.2.2 2 3 8 | less

#### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_mo%C5%BEn%C3%A9-probl%C3%A9my-v-opera%C4%8Dn%C3%ADm-syst%C3%A9mu-windows)Possible problems in the windows operating system

In some Windows installations, there is a problem with the standard virtual machine configuration. If the virtual tester cannot connect to the server under test on the host operating system, use the following procedure:

-   With the tester virtual machine turned off, change the network adapter settings from NAT to Host-only network.
-   The network interface belonging to VirtualBox should appear in the host OS. This can be found from the command line with the *ipconfig* command . The IP address of this interface will probably be 192.168.56.1/24.
-   In the virtual tester, it is now necessary to manually set the IP address of the eth0 network interface:

sudo ifconfig eth0 192.168.56.2 netmask 255.255.255.0

-   It is now possible to run the tester, but enter the IP address of the network interface in the host OS as the destination address:

tester 3999 192.168.56.1

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_ke-sta%C5%BEen%C3%AD)Download

VirtualBox application: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

Tester: [All versions of the tester for download](https://drive.google.com/drive/folders/1QzPyzZeLNWZhjtbaTGehyNu-zgHcInta?usp=sharing)

The directory from the previous link contains directories with development versions of the tester. You will find the following files in each directory labeled vX (where *X* is the version number):

-   BI-PSI\_tester\_2021\_vX.ova - virtual with tester
-   psi-tester-2021-vX\_x64.bz2 - version for linux 64-bit
-   psi-tester-2021-vX\_x86.bz2 - version for linux 32-bit

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_po%C5%BEadavky-na-%C5%99e%C5%A1en%C3%AD)Solution requirements
------------------------------------------------------------------------------------------------------------------------

-   The solution can be created in any programming language.

-   Only a solution that passes all the tests will be accepted.

[](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_odevzd%C3%A1n%C3%AD)Submission
-----------------------------------------------------------------------------------------

The task is successfully submitted only if the source code has been uploaded to the submission server and the solution has been personally presented in a laboratory exercise! The date of submission is determined by uploading to the submission server, so it is possible to present the task even after the deadline and without penalty.

###### Důležité:

**DEADLINE for upload without penalty is 2. 5. 2021!**

###### Důležité:

**After this date, the maximum number of points available will be reduced by two for each week started. In the last week of the semester, a maximum of 6 points can be obtained!**

###### Důležité:

**The task must be presented no later than the end of the credit week!**

On the other hand, early submission will be rewarded with points for activity. Each week in advance will be honored with one point up to a maximum of 5 points. Schedule of possible bonus points:

-   to 28.3. +5 points
-   up to 4.4 +4 points
-   to 11.4. +3 points
-   to 18.4. +2 points
-   to 25.4. +1 point

Activity points will not be awarded in bulk (or corrected) until the end of the semester, when the submission of assignments is completed. The points will of course be calculated on the date of uploading to the archive server before the presentation.

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_n%C3%A1hr%C3%A1n%C3%AD-na-archiva%C4%8Dn%C3%AD-server)Upload to archive server

A special server (PSI shed) is used for submission. **Each student registers with it and will record their ongoing solutions in their own interest, so that everyone has a traceable history in case of suspected plagiarism.**When registering on the server, it is necessary to select a programming language. If you need to change it, contact the server administrator ( [cernyvi2@fit.cvut.cz](mailto:cernyvi2@fit.cvut.cz) ). At the end of the semester, all submitted source codes will be tested for duplication. If two or more codes match, ongoing submissions can help. The source code is loaded in one file and uncompressed. The submission server does not check the code, it only compares it with the codes of other students and looks for a match. Thus, it is possible to combine multiple source codes into one, even if such code is then uncomplicable without modification.

###### Tip:

Write your code in a single file. This will make your handover much easier.

###### Tip:

If you have a solution divided into several files, all you have to do is combine their contents into one. The resulting file may not be compilable, but must contain all of your solution's source code. On Linux, you can merge files with a simple command: cat \* .java\> all.java

Link to submission server: [PSI shed](https://bouda.fit.cvut.cz/)

###### Důležité:

If you did not find your favorite language on the menu, complain here: [cernyvi2@fit.cvut.cz](mailto:cernyvi2@fit.cvut.cz) .

###### Důležité:

If you did not receive an authentication email within 24 hours, complain here: [cernyvi2@fit.cvut.cz](mailto:cernyvi2@fit.cvut.cz) .

### [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html#_osobn%C3%AD-prezentace)Personal presentation

Presentations are possible only during laboratory hours, in even and odd weeks, unless the teacher determines otherwise. It can be presented no later than the end of the credit week. During the presentation, the student must demonstrate that the code understands and that the code works. The code that is presented must be the same as the one submitted to the submission server. The check is performed in the following steps:

1.  The student proves his / her identity.
2.  The student shows the source code and runs the test so that it is clear that the presented code is being tested.
3.  The student answers the control questions to the source code.
4.  The student uploads the source code to the submission server so that it is clear that he is uploading the really presented code.

It is up to each student to ensure the smooth running of all these steps. If any of the above cannot be met, agree with your trainer how to proceed.

###### Tip:

Present the task as soon as possible after the final upload to the Bouda server. The longer you delay the presentation, the more you risk forgetting the implementation details and not being convincing enough that you understand the implementation.

Prohlížíte verzi **...**.
 [Přejděte na aktuální verzi.](https://courses.fit.cvut.cz/BI-PSI/)

Subject navigation
==================

-   [](https://courses.fit.cvut.cz/BI-PSI/index.html)
    BI-PSI
-   [](https://courses.fit.cvut.cz/BI-PSI/annotation/index.html)
    Annotation
-   [](https://courses.fit.cvut.cz/BI-PSI/homework/index.html)
    Homework
-   [](https://courses.fit.cvut.cz/BI-PSI/fitnetcamp2021/index.html)
    FITNET Camp 2021
-   [](https://courses.fit.cvut.cz/BI-PSI/classification/index.html)
    Evaluation
-   [](https://courses.fit.cvut.cz/BI-PSI/parttime/index.html)
    Combined Studies
    -   [](https://courses.fit.cvut.cz/BI-PSI/parttime/lectures.html)
        Přednášky
-   [](https://courses.fit.cvut.cz/BI-PSI/labs/index.html)
    A Lab exercise
    -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/index.html)
        Laboratorní úlohy
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/manuals/index.html)
            Návody
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/manuals/manual-cisco.html)
                Konfigurace CISCO
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/manuals/manual-linux.html)
                Konfigurace LINUX
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/manuals/linux-image.html)
                Netlab image
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/manuals/laboratory.html)
                Síťová laboratoř
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/lab1.html)
            Úloha č. 1
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/lab2.html)
            Úloha č. 2
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/lab3.html)
            Úloha č. 3
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/lab4.html)
            Úloha č. 4
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks/lab5.html)
            Úloha č. 5
    -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/index.html)
        Laborky
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/lab1.html)
            Laborka 1
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/lab2.html)
            Laborka 2
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/lab3.html)
            Laborka 3
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/lab4.html)
            Laborka 4
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/lab5.html)
            Laborka 5
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/manuals/index.html)
            Návody
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/manuals/manual-cisco.html)
                Konfigurace CISCO
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/manuals/manual-linux.html)
                Konfigurace OpenWRT
            -   [](https://courses.fit.cvut.cz/BI-PSI/labs/tasks_home_study/manuals/manual-gns3.html)
                Síťový emulátor GNS3
    -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/index.html)
        Základní pojmy
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/arp.html)
            Address resolution protocol (ARP)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/dhcp.html)
            DHCP (Dynamic Host Configuration Protocol)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/dns.html)
            Doménový server (DNS)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/firewall.html)
            Firewall
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/ip-adresa.html)
            IP adresa
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/iso-osi.html)
            ISO-OSI model
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/lan.html)
            Lokální síť (LAN)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/mac-adresa.html)
            MAC adresa
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/hub.html)
            Opakovač (Repeater, Hub)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/ports.html)
            Porty TCP/UDP
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/nat.html)
            Překlad adres (NAT)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/switch.html)
            Přepínač (switch)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/network-interface.html)
            Síťové rozhraní (Network interface)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/router.html)
            Směrovač (Router)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/routing.html)
            Směrování (Routing)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/connection.html)
            Spojení (TCP) (Connection (TCP))
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/tcp.html)
            Transmission Control Protocol (TCP)
        -   [](https://courses.fit.cvut.cz/BI-PSI/labs/basic-terms/udp.html)
            User Datagram Protocol (UDP)
-   [](https://courses.fit.cvut.cz/BI-PSI/lectures/index.html)
    Lectures
-   [](https://courses.fit.cvut.cz/BI-PSI/seminars/index.html)
    Proseminars
-   [](https://courses.fit.cvut.cz/BI-PSI/teacher/index.html)
    Teachers
-   [](https://courses.fit.cvut.cz/BI-PSI/exam/index.html)
    Exam

Homework
 [homework / index.adoc](https://gitlab.fit.cvut.cz/BI-PSI/bi-psi/blob/master/homework/index.adoc) , [last modified 251cdbe2 (3. 5. 2021 at 13:03, Ing. Viktor Černý)](https://gitlab.fit.cvut.cz/BI-PSI/bi-psi/commit/251cdbe2a1fec9d0edfecfd70efa2a51b92f9c65 "Update homework / index.adoc")

Generated by [**FIT CTU Course Pages**](https://gitlab.fit.cvut.cz/course-pages/course-pages/) v0.8.0
 Page generated5. 11. 2021 at 18:20

[![Build status](./TCP_files/pipeline.svg)](https://gitlab.fit.cvut.cz/BI-PSI/bi-psi/pipelines)

![Google Translate](./TCP_files/translate_24dp.png)

Original text
=============

Contribute a better translation

* * * * *
