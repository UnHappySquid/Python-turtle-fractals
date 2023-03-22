import turtle
import math
import sys
import time

def carre(t,length):
    if length < 2:
        t.fd(length)
        return
    carre(t,length/3)
    t.lt(90)
    carre(t, length / 3)
    t.right(90)
    carre(t, length / 3)
    t.right(90)
    carre(t,length/3)
    t.lt(90)
    carre(t,length/3)

def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)

def minkowski(t,length):
    if length < 10:
        t.fd(length)
        return
    minkowski(t, length / 4)
    t.lt(90)
    minkowski(t, length / 4)
    t.rt(90)
    minkowski(t, length / 4)
    t.rt(90)
    minkowski(t, length / 4)
    minkowski(t, length / 4)
    t.lt(90)
    minkowski(t, length / 4)
    t.lt(90)
    minkowski(t, length / 4)
    t.rt(90)
    minkowski(t, length / 4)

def cesaro(t,length, inputangle=60):
    '''input angle has to be between 45 (exlusive) and 90 (simple grid) degrees'''
    angle = 90 - inputangle
    angle = math.radians(angle)

    if length < (10):
        t.fd((1/math.tan(angle))*length)
        return

    d = length * math.tan(angle)

    length = (length - d) / 2

    cesaro(t, length,inputangle)
    t.lt(inputangle)
    cesaro(t, length, inputangle)
    t.rt(2*inputangle)
    cesaro(t, length,inputangle)
    t.lt(inputangle)
    cesaro(t, length,inputangle)

#USE MINKOWSKI

#seems to have a certain symetry (unlike carree)
def minkowskiSnowflake(t,length):
    minkowski(t,length)
    t.lt(90)
    minkowski(t, length)
    t.lt(90)
    minkowski(t, length)
    t.lt(90)
    minkowski(t, length)
    t.lt(90)

def minkowskiCarre(t,length):
    minkowski(t,length)
    t.rt(90)
    minkowski(t, length)
    t.rt(90)
    minkowski(t, length)
    t.rt(90)
    minkowski(t, length)
    t.rt(90)

#USE CARRE
def carreSnowflake(t,length):
    carre(t,length)
    t.lt(90)
    carre(t, length)
    t.lt(90)
    carre(t, length)
    t.lt(90)
    carre(t, length)
    t.lt(90)

def carreCarre(t,length):
    carre(t,length)
    t.rt(90)
    carre(t, length)
    t.rt(90)
    carre(t, length)
    t.rt(90)
    carre(t, length)
    t.rt(90)

#USE KOCH
def kochSnowflake(t,length):
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)

def cesaroAntisnowflake(t,length):
    koch(t, length)
    t.lt(90)
    koch(t, length)
    t.lt(90)
    koch(t, length)
    t.lt(90)
    koch(t,length)
    t.lt(90)

def kochAntisnowflake(t,length):
    koch(t, length)
    t.lt(120)
    koch(t, length)
    t.lt(120)
    koch(t, length)
    t.lt(120)


#USE KOCHANTISNOWFLAKE
def kochAntisnowflakePlane(t,length):
    for i in range(6):
        kochAntisnowflake(t,length)
        t.lt(60)


def choice():
   
    print("Please enter a number corresponding to the desired shaped: \n")
 
    
    for i in switcher:
        if (i == 99):
            print("\t99\t:\tTo exit\n")
            continue
        print(f"\t{i}\t:\t{switcher[i].__name__}\n")

    print("Note that the turtle who will be serving you is named bob\n")

    read = input()
    if (not read.isnumeric() or (int(read) > 12 and int(read) != 99)):
        print(f"{read} is a bad input, please try again")
    elif(int(read) == 99):
        exit("Good bye!")
    else:
        print("\nNow Enter the desired size of the drawing, please keep it small bob can only go so fast :(\n")
        size_read = input()
        if (not size_read.isnumeric()):
            print(f"{size_read} is not a valid size")
        else:
            chosen = int(read)
            size = int(size_read)
            bob.clear()
            bob.pu()
            bob.goto(- (size / 2),- (size / 2))
            bob.pd()
            switcher[chosen](bob, size)
            time.sleep(5)
    choice()

        
    


if __name__ == "__main__":
    
    switcher = {
        1: carre,
        2: koch,
        3: minkowski,
        4: cesaro,
        5: minkowskiSnowflake,
        6: minkowskiCarre,
        7: carreSnowflake,
        8: carreCarre,
        9: kochSnowflake,
        10: cesaroAntisnowflake,
        11: kochAntisnowflake,
        12: kochAntisnowflakePlane,
        99: exit
    }
            
    bob = turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    
    # setting the background black
    bob.getscreen().bgcolor(0, 0, 0)
    # setting the line white
    bob.color("white")
    



    args = sys.argv
    
    if (len(args) > 2):
        size = int(args[1])
    
        for i in range(2, len(args)):
            input = int(args[i])
            
            if (input <= 12):
                bob.clear()
                bob.pu()
                bob.goto(- (size / 2),- (size / 2))
                bob.pd()
                switcher[input](bob, size)
                time.sleep(5)

        exit()

    choice()
