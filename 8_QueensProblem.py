#import random for generating random populations
import random
#generation of 4 population and choosing two different childs
#intiliazed 6 arrays
listarr1=[]
listarr2=[]
listarr3=[]
listarr4=[]
childarr1=[]
childarr2=[]
#global variables
global bool
global second_maximum
global fitness
global count
global x_positive_up
global x_positive_down
global y_positive_up
global y_positive_down
global x_negative_up
global x_negative_down
global y_negative_up
global y_negative_down
global largest


#random generator for placing queen at different places
def arrgenerator (d):
    i = 0
    while i < 8:
        d.append(random.randint(1, 8))
        i += 1

arrgenerator(listarr1)
arrgenerator(listarr2)
arrgenerator(listarr3)
arrgenerator(listarr4)

print("POPULATIONS:")
board1 = [[0] * (8) for i in range(8)]
board2 = [[0] * (8) for i in range(8)]
board3 = [[0] * (8) for i in range(8)]
board4 = [[0] * (8) for i in range(8)]
board5 = [[0] * (8) for i in range(8)]
board6 = [[0] * (8) for i in range(8)]


#function for making board
def makeboard(l, b):
    count = 0
    for i in l:
        b[i-1][count] = 1
        count = count + 1

#Representation of populations in boards
makeboard(listarr1, board1)
makeboard(listarr2, board2)
makeboard(listarr3, board3)
makeboard(listarr4, board4)


#calculate the fitness function of the population generated
def fitnessfunction(board, listarr):
    ftiness = 0
    for i in range(8):
        bool = True
        r = listarr[i]-1
        c = i
        for z in range(8):
            if c == z:
                continue
            elif board[r][z] == 1:
                bool = False
                break

        if (bool==True):
            x_positive_up = r - 1
            y_positive_up = c + 1
            while x_positive_up >= 0 and y_positive_up <= 7:
                if board[x_positive_up][y_positive_up] == 1:
                    bool = False
                    break
                x_positive_up = x_positive_up - 1
                y_positive_up = y_positive_up + 1

        if (bool==True):
            x_positive_down = r + 1
            y_positive_down = c - 1
            while x_positive_down <= 0 and y_positive_down >= 7:
                if board[x_positive_down][y_positive_down] == 1:
                    bool = False
                    break
                x_positive_down = x_positive_down + 1
                y_positive_down = y_positive_down - 1

        if (bool==True):
            x_negative_up = r + 1
            y_negative_up = c + 1
            while x_negative_up <= 7 and y_negative_up <= 7:
                if board[x_negative_up][y_negative_up] == 1:
                    bool = False
                    break
                x_negative_up = x_negative_up + 1
                y_negative_up = y_negative_up + 1

        if (bool==True):
            x_negative_down = r - 1
            y_negative_down = c - 1
            while x_negative_down >= 0 and y_negative_down >= 0:
                if board[x_negative_down][y_negative_down] == 1:
                    bool = False
                    break
                x_negative_down = x_negative_down - 1
                y_negative_down = y_negative_down - 1

        if(bool==True):
            ftiness = ftiness + 1
    return ftiness

fitnessarr = [(fitnessfunction(board1, listarr1)), (fitnessfunction(board2, listarr2)), (fitnessfunction(board3, listarr3)), (fitnessfunction(board4, listarr4))]

#function to choose best two child among 4 population generated
def first_maximum(arr):
    second_maximum = arr[0]
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > second_maximum and arr[i] != largest:
            second_maximum = arr[i]

    return second_maximum




#function to select parents after choosing the two most fit populations
def parent_selection():
    global childarr1
    global childarr2
    makeboard(listarr1, board1)
    makeboard(listarr2, board2)
    makeboard(listarr3, board3)
    makeboard(listarr4, board4)
    fitnessarr = [(fitnessfunction(board1, listarr1)), (fitnessfunction(board2, listarr2)), (fitnessfunction(board3, listarr3)),
                  (fitnessfunction(board4, listarr4))]

    arr_index_1 = fitnessarr.index(max(fitnessarr)) +1
    arr_index_2 = fitnessarr.index(first_maximum(fitnessarr)) + 1



    if arr_index_1 == 1:
        childarr1 = listarr1[0:4].copy()
        childarr2 = listarr1[4:8].copy()
    if arr_index_1 == 2:
        childarr1 = listarr2[0:4].copy()
        childarr2 = listarr2[4:8].copy()
    if arr_index_1 == 3:
        childarr1 = listarr3[0:4].copy()
        childarr2 = listarr3[4:8].copy()
    if arr_index_1 == 4:
        childarr1 = listarr4[0:4].copy()
        childarr2 = listarr4[4:8].copy()

    if arr_index_2 == 1:
        childarr1 = childarr1 + listarr1[4:8]
        childarr2 = listarr1[0:4] + childarr2
    if arr_index_2 == 2:
        childarr1 = childarr1 + listarr2[4:8]
        childarr2 = listarr2[0:4] + childarr2
    if arr_index_2 == 3:
        childarr1 = childarr1 + listarr3[4:8]
        childarr2 = listarr3[0:4] + childarr2
    if arr_index_2 == 4:
        childarr1 = childarr1 + listarr4[4:8]
        childarr2 = listarr4[0:4] + childarr2

#mutation of one chosen index in the given population
def mutate(childarr):
    mutationindex = (random.randint(0, 7))
    childarr[mutationindex] = (random.randint(1, 8))

#choose one parent from the two maximum fitness child
parent_selection()
population = [childarr1, childarr2]

mutate(childarr1)
mutate(childarr2)

makeboard(childarr1, board5)
makeboard(childarr2, board6)

fitnessarr.append(fitnessfunction(board5, childarr1))
fitnessarr.append(fitnessfunction(board6, childarr2))
print(listarr1, listarr2, listarr3, listarr4)

def remove():
    global listarr1, listarr2, listarr3, listarr4,childarr1,childarr2
    all = []

    makeboard(childarr1, board5)
    makeboard(childarr2, board6)
    makeboard(listarr1, board1)
    makeboard(listarr2, board2)
    makeboard(listarr3, board3)
    makeboard(listarr4, board4)
    all.append([fitnessfunction(board1, listarr1), listarr1])
    all.append([fitnessfunction(board2, listarr2), listarr2])
    all.append([fitnessfunction(board3, listarr3), listarr3])
    all.append([fitnessfunction(board4, listarr4), listarr4])
    all.append([fitnessfunction(board5, childarr1), childarr1])
    all.append([fitnessfunction(board6, childarr2), childarr2])

    all.sort(key=lambda x: x[0],reverse=True)

    listarr1=all[0][1]
    listarr2 = all[1][1]
    listarr3 = all[2][1]
    listarr4 = all[3][1]

#prints boards of the selected population
def printboard (n):
    for i in n:
        print(i)

print()
print("Fitness Value", (fitnessfunction(board1, listarr1)))
printboard(board1)
print()
print("Fitness Value", (fitnessfunction(board2, listarr2)))
printboard(board2)
print()
print("Fitness Value:", (fitnessfunction(board3, listarr3)))
printboard(board3)
print()
print("Fitness Value:", (fitnessfunction(board4, listarr4)))
printboard(board4)
print()
print(fitnessarr)
print("Crossover effect: " + str(population))
print("Mutation effect: ", childarr1, childarr2)
print()
count=0
remove()

while fitnessfunction(board1, listarr1)<=8  and count<10:
    count+=1
    population = [childarr1, childarr2]
    print("The Parents are: " + str(population))
    parent_selection()
    population = [childarr1, childarr2]
    print("Crossover Effect : " + str(population))
    mutate(childarr1)
    mutate(childarr2)
    population = [childarr1, childarr2]
    print("Mutation Effect: " + str(population))
    print()
    remove()

print("fitness of the population printed below is")
print(fitnessfunction(board1, listarr1))
print(listarr1)



