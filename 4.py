
arr = [[1,2],[3,4]]
movesList = []

moves = input()
n = 0

pool = multiprocessing.Pool(processes=2)

for letter in moves:
    movesList.append(letter)


while n < len(movesList):
        move = movesList[0]

        if move == "H":
            E = arr[0]
            arr[0] = arr[1]
            arr[1] = E
            movesList.pop(0)
        else:
            E = arr[0][0]
            arr[0][0] = arr[0][1]
            arr[0][1] = E
            E = arr[1][0]
            arr[1][0] = arr[1][1]
            arr[1][1] = E
            movesList.pop(0)
            
print(str(arr[0][0]) + " " + str(arr[0][1]))
print(str(arr[1][0]) + " " + str(arr[1][1]))




