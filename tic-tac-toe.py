from random import randrange

bd = {}
list_number = [5]

def printboard():

    global bd
    bd[(1,1)] = 'X'

    print("+-----------+-----------+-----------+")
    print("|           |           |           |")
    print("|    {}      |    {}      |    {}      |".format(bd[(0,0)], bd[(0,1)], bd[(0,2)]))
    print("|           |           |           |")
    print("+-----------+-----------+-----------+")
    print("|           |           |           |")
    print("|    {}      |    {}      |    {}      |".format(bd[(1,0)], bd[(1,1)], bd[(1,2)]))
    print("|           |           |           |")
    print("+-----------+-----------+-----------+")
    print("|           |           |           |")
    print("|    {}      |    {}      |    {}      |".format(bd[(2,0)], bd[(2,1)], bd[(2,2)]))
    print("|           |           |           |")
    print("+-----------+-----------+-----------+")
            
            

def DrawBoard():

    global bd
    i = 0

    for row in range(3):
        for column in range(3):
            tp = (row,column)
            i = i + 1
            bd.update({tp:i})
            
    #for key in sorted(bd.keys()):
    #    print(key, "->", bd[key])

    printboard()

def YboardM():

    global bd
    global list_number
    move_state = True

    while move_state:

        ym = int(input("Enter your move: "))

        if ym < 1 or ym > 9:
            print("Enter correct move")
            continue
        else:
            if ym not in list_number:
                list_number.append(ym)
                for row in range(3):
                    for column in range(3):
                        if bd[(row,column)] == ym:
                            bd[(row,column)] = '0'
                            move_state = False
                            break
            else:
                print(f"Your move {ym} is already taken. Try different move")
                continue

    printboard()
    result = Checkwin()

    if result != 'finish':
        CboardM()
    


def CboardM():

    global bd
    global list_number

    move_state = True
    
    while move_state:
        number = randrange(1,9)
        if number not in list_number:
            list_number.append(number)
            for row in range(3):
                for column in range(3):
                    if bd[(row,column)] == number:
                        bd[(row,column)] = 'X'
                        move_state = False
                        break
        else:
            continue

    printboard()
    result = Checkwin()

    if result != 'finish':
        YboardM()

def Checkwin():

    global bd

    if bd[(0,0)] == '0' and bd[(0,1)] == '0' and bd[(0,2)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(1,0)] == '0' and bd[(1,1)] == '0' and bd[(1,2)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(2,0)] == '0' and bd[(2,1)] == '0' and bd[(2,2)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(0,0)] == '0' and bd[(1,0)] == '0' and bd[(2,0)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(0,1)] == '0' and bd[(1,1)] == '0' and bd[(2,1)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(0,2)] == '0' and bd[(1,2)] == '0' and bd[(2,2)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(0,0)] == '0' and bd[(1,1)] == '0' and bd[(2,2)] == '0':
        print("YOU WON")
        return 'finish'
    elif bd[(0,2)] == '0' and bd[(1,1)] == '0' and bd[(2,0)] == '0':
        print("YOU WON")
        return 'finish'

    if bd[(0,0)] == 'X' and bd[(0,1)] == 'X' and bd[(0,2)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(1,0)] == 'X' and bd[(1,1)] == 'X' and bd[(1,2)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(2,0)] == 'X' and bd[(2,1)] == 'X' and bd[(2,2)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(0,0)] == 'X' and bd[(1,0)] == 'X' and bd[(2,0)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(0,1)] == 'X' and bd[(1,1)] == 'X' and bd[(2,1)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(0,2)] == 'X' and bd[(1,2)] == 'X' and bd[(2,2)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(0,0)] == 'X' and bd[(1,1)] == 'X' and bd[(2,2)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    elif bd[(0,2)] == 'X' and bd[(1,1)] == 'X' and bd[(2,0)] == 'X':
        print("COMPUTER WON")
        return 'finish'
    
            
DrawBoard()
YboardM()


