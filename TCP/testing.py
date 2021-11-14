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



def main():

    cx = 8
    cy = 0
    direction = 'RIGHT'
    commands = movetogoal(cx,cy,direction)
    print(commands)

if __name__ == '__main__':
    main()
