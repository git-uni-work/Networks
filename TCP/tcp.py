import os
import socket
from threading import Thread
from time import sleep

############################################################
SERVER_MOVE = '102 MOVE\a\b'.encode('utf-8')
SERVER_TURNLEFT = '103 TURN LEFT\a\b'.encode('utf-8')
SERVER_TURNRIGHT = '104 TURN RIGHT\a\b'.encode('utf-8')
SERVER_PICKUP = '105 GET MESSAGE\a\b'.encode('utf-8')
SERVER_LOGOUT = '106 LOGOUT\a\b'.encode('utf-8')
SERVER_OK = '200 OK\a\b'.encode('utf-8')
SERVER_LOGINFAILED = '300 LOGIN FAILED\a\b'.encode('utf-8')
SERVER_SYNTAXERROR = '301 SYNTAX ERROR\a\b'.encode('utf-8')
SERVER_LOGICERROR = '302 LOGIC ERROR\a\b'.encode('utf-8')

CLIENT_RECHARGING = 'RECHARGING\a\b'
CLIENT_FULLPOWER = 'FULL POWER\a\b'

USERNAME_LEN = 10
CONFIRMATION_LEN = 5
OK_LEN = 10
RECHARGING_LEN = 10
FULLPOWER_LEN = 10
MESSAGE_LEN = 98

CLIENT_KEY = 45328
SERVER_KEY = 54621
############################################################
def snake( direction ):
    directions = []
    if ( direction == 'UP'):
        directions.append('RIGHT')
        directions.append('RIGHT')
    if ( direction == 'RIGHT'):
        directions.append('RIGHT')
    if ( direction == 'LEFT'):
        directions.append('LEFT')

    for x in range( 0 , 3):
        for y in range ( 0 ,4 ):
            directions.append("UP")
        directions.append("RIGHT")
    for x in range( 0 , 2):
        for y in range ( 0 ,3 ):
            directions.append("UP")
        directions.append("RIGHT")
    for x in range( 0 , 2):
        for y in range ( 0 ,2 ):
            directions.append("UP")
        directions.append("RIGHT")
    for x in range( 0 , 2):
        for y in range ( 0 ,1 ):
            directions.append("UP")
        directions.append("RIGHT")

    return directions

def movetogoal( cx , cy , direction ):
    directions = []
    goalx = 2
    goaly = 2

    while True:

        if cx == goalx and cy == goaly:
            break

        if ( cx < goalx and direction == 'UP' ):
            directions.append('RIGHT')
            direction = 'RIGHT'
            continue
        elif (cx < goalx and direction == 'DOWN'):
            directions.append('RIGHT')
            directions.append('RIGHT')
            direction = 'UP'
            continue
        elif (cx < goalx and direction == 'RIGHT'):
            directions.append('UP')
            direction = 'RIGHT'
            cx = cx + 1
            continue
        elif (cx < goalx and direction == 'LEFT'):
            directions.append('LEFT')
            direction = 'LEFT'
            continue
        elif (cx > goalx and direction == 'UP'):
            directions.append('LEFT')
            direction = 'LEFT'
            continue
        elif (cx > goalx and direction == 'DOWN'):
            directions.append('RIGHT')
            directions.append('RIGHT')
            direction = 'UP'
            continue
        elif (cx > goalx and direction == 'RIGHT'):
            directions.append('LEFT')
            directions.append('LEFT')
            direction = 'LEFT'
            continue
        elif (cx > goalx and direction == 'LEFT'):
            directions.append('UP')
            direction = 'LEFT'
            cx = cx - 1
            continue
        else:
            if (cy < goaly and direction == 'UP'):
                directions.append('UP')
                direction = 'UP'
                cy = cy + 1
                continue
            elif (cy < goaly and direction == 'DOWN'):
                directions.append('RIGHT')
                directions.append('RIGHT')
                direction = 'UP'
                continue
            elif (cy < goaly and direction == 'RIGHT'):
                directions.append('LEFT')
                direction = 'UP'
                continue
            elif (cy < goaly and direction == 'LEFT'):
                directions.append('RIGHT')
                direction = 'UP'
                continue
            elif (cy > goaly and direction == 'UP'):
                directions.append('LEFT')
                directions.append('LEFT')
                direction = 'DOWN'
                continue
            elif (cy > goaly and direction == 'DOWN'):
                directions.append('UP')
                direction = 'DOWN'
                cy = cy - 1
                continue
            elif (cy > goaly and direction == 'RIGHT'):
                directions.append('RIGHT')
                direction = 'DOWN'
                continue
            elif (cy > goaly and direction == 'LEFT'):
                directions.append('LEFT')
                direction = 'DOWN'
                continue

    return directions

def getxy(data):
    x = 0
    y = 0
    tmp = data.split(' ')
    x = int(tmp[1])
    y = int(tmp[2])
    return x , y

def confirm(check , oghash):
    check += 65536 - CLIENT_KEY
    check %= 65536
    if check == oghash:
        return True
    else:
        return False

def hashfx(username):
    asciivalue = 0
    for char in username:
        asciivalue += ord(char)
    asciivalue *= 1000

    hash = asciivalue % 65536
    serverconfirm = (SERVER_KEY + hash) % 65536
    serverconfirmation = presend(serverconfirm)
    return serverconfirmation , hash

def presend(message):
    message = str(message)
    message += '\a\b'
    return message.encode('utf-8')

def validate ( message , authenticated , found , flag ):
    length = len(message)
    if length == 0:
        return message , 'empty'

    if message == 'RECHARGING' or message == 'FULL POWER':
        if length <= RECHARGING_LEN:
            print('**VALID RECHARGING / FULLPOWER**')
            return message ,'recharging'
        else:
            return message , 'error'


    if not authenticated:
        if length <= USERNAME_LEN:
            print("**VALID USERNAME**")
            return message ,'username'
        else:
            return message , 'error'

    else:
        if authenticated and not flag:
            if length <= CONFIRMATION_LEN:
                print("**VALID CONFIRMATION**")
                return message ,'confirmation'
        if not found and message != '' and message[0] == 'O' and message[1] == 'K' and message[2] == ' ':
            if length <= OK_LEN:
                print("**VALID COORDINATES**")
                return message ,'coordinates'
            else:
                return message, 'error'
        else:
            if length <= MESSAGE_LEN:
                print("**VALID MESSAGE**")
                return message, 'secret'
            else:
                return message, 'error'

def initsocket():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1999))
    server.listen(1)
    return server

class server:

    def __init__(self):
        self.threads = []

    def newconnection(self,socket):

        while True:
            client, address = socket.accept()
            client.settimeout(1)
            thread = Thread(target=self.communicate , args=(socket,client,address))
            thread.start()
            self.threads.append(thread)

    def communicate(self,socket,client,address):

        try:
            data = ''
            counter = 0
            authenticated = False
            found = False
            flag = False
            hash = 0
            previousx = 0
            previousy = 0
            tmpcounter = 0
            tmpc = -1
            secretflag = 1
            charging = False
            byte = client.recv(1).decode('utf-8')
            data += byte

            while True:
                byte = client.recv(1).decode('utf-8')

                if data[counter] == '\a' and byte == '\b':
                    data += byte
                    data = data[0:counter]
                    print('YE')

                    validdata, type = validate(data, authenticated, found, flag)
                    # print(validdata)

                    if type == 'error':
                        client.sendall(SERVER_SYNTAXERROR)
                        break

                    if type == 'recharging':
                        if validdata == 'RECHARGING':
                            client.settimeout(5)
                            charging = True
                            data = ''
                            counter = 0
                            byte = client.recv(1).decode('utf-8')
                            data += byte
                            print('CHARGIN...')
                            continue

                        if validdata == 'FULL POWER':
                            client.settimeout(1)
                            charging = False
                            data = ''
                            counter = 0
                            byte = client.recv(1).decode('utf-8')
                            data += byte
                            print('FULL POWER!')
                            continue

                    if charging:
                        print('CHARGING ERROR!')
                        client.sendall(SERVER_LOGICERROR)
                        break


                    if type == 'username':
                        authenticated = True
                        validdata, hash = hashfx(validdata)
                        client.sendall(validdata)
                        data = ''
                        counter = 0
                        byte = client.recv(1).decode('utf-8')
                        data += byte
                        print('==USERNAME AUTHENTICATED==')
                        continue

                    if type == 'confirmation':
                        if confirm(int(validdata), hash):
                            client.sendall(SERVER_OK)
                            client.sendall(SERVER_MOVE)
                            data = ''
                            counter = 0
                            byte = client.recv(1).decode('utf-8')
                            data += byte
                            print('==HASH CONFIRMED==')
                            continue
                        else:
                            client.sendall(SERVER_LOGINFAILED)
                            break

                    if type == 'secret':
                        print("!!!SECRET MESSAGE FOUND!!!")
                        print('"', validdata, '"')
                        client.sendall(SERVER_LOGOUT)
                        break

                    if type == 'coordinates' or type == 'empty':
                        flag = True

                        if type == 'coordinates':
                            currentx , currenty = getxy(validdata)

                        if previousx == 0 and previousy == 0:
                            previousx = currentx
                            previousy = currenty
                            client.sendall(SERVER_MOVE)
                            data = ''
                            counter = 0
                            byte = client.recv(1).decode('utf-8')
                            data += byte
                            print('1st MOVE')
                            continue
                        elif previousx == currentx and previousy == currenty:
                            client.sendall(SERVER_MOVE)
                            data = ''
                            counter = 0
                            byte = client.recv(1).decode('utf-8')
                            data += byte
                            print('MOVE!')
                            continue
                        else:
                            if previousx > currentx:
                                direction = 'LEFT'
                            elif previousx < currentx:
                                direction = 'RIGHT'
                            elif previousy > currenty:
                                direction = 'DOWN'
                            else:
                                direction = 'UP'

                            # print("current = ", currentx, currenty)
                            # print("previous = ", previousx, previousy)
                            # print("direction = ",direction)

                            if tmpc == -1:
                                if currentx == 2 and currenty == 2:
                                    tmpc = 0
                                    commands = snake(direction)

                            if tmpc >= 0:
                                if secretflag:
                                    client.sendall(SERVER_PICKUP)
                                    data = ''
                                    counter = 0
                                    byte = client.recv(1).decode('utf-8')
                                    data += byte
                                    secretflag = 0
                                    continue
                                if type == 'empty':
                                    if commands[tmpc] == 'UP':
                                        client.sendall(SERVER_MOVE)
                                        data = ''
                                        counter = 0
                                        byte = client.recv(1).decode('utf-8')
                                        data += byte
                                        print('~SNAKE FORWARD~')
                                        tmpc += 1
                                        previousx = currentx
                                        previousy = currenty
                                        secretflag = 1
                                        continue
                                    elif commands[tmpc] == 'RIGHT':
                                        client.sendall(SERVER_TURNRIGHT)
                                        print('~SNAKE RIGHT~')
                                        data = ''
                                        counter = 0
                                        byte = client.recv(1).decode('utf-8')
                                        data += byte
                                        tmpc += 1
                                        secretflag = 1
                                        continue

                            if tmpcounter == 0:
                                listofmoves = movetogoal(currentx,currenty,direction)
                            if listofmoves[tmpcounter] == 'UP':
                                client.sendall(SERVER_MOVE)
                                data = ''
                                counter = 0
                                byte = client.recv(1).decode('utf-8')
                                data += byte
                                print('--MOVIN FORWARD--')
                                tmpcounter += 1
                                previousx = currentx
                                previousy = currenty
                                continue
                            elif listofmoves[tmpcounter] == 'RIGHT':
                                client.sendall(SERVER_TURNRIGHT)
                                print('--TURNED RIGHT--')
                                data = ''
                                counter = 0
                                byte = client.recv(1).decode('utf-8')
                                data += byte
                                tmpcounter += 1
                                continue
                            elif listofmoves[tmpcounter] == 'LEFT':
                                client.sendall(SERVER_TURNLEFT)
                                print('--TURNED LEFT--')
                                data = ''
                                counter = 0
                                byte = client.recv(1).decode('utf-8')
                                data += byte
                                tmpcounter += 1
                                continue

                else:
                    data += byte
                    counter += 1
                    continue

        except socket.timeout:
            print("TIMEOUT! - ENDING CONNECTION")

        finally:
            print("SERVER - CLOSED")
            client.close()


def main():

    moiserver = server()
    socket = initsocket()
    moiserver.newconnection(socket)

    print('YE YE')

if __name__ == '__main__':
    main()
