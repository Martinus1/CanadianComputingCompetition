N = int(input())


i = 0
z = 0

string = ""

arr = [[] for n in range (N)]
current = ""
times = 0
u = 0


while (i < N) :
    current = ""
    times = 0
    text = input()
    
    for num in text :
        if current == "":
            current = num
            times = times + 1
            
        elif current == num:
            times = times + 1
        else:
s
            arr[i].append(str(times))
            arr[i].append(current)
            current = num
            times = 1
            
    arr[i].append(str(times))
    arr[i].append(current)    
    i = i + 1
    

for element in arr:
    for ele in element:
        string = string + " " + ele
        u = u + 1
    print(string)
    string = ""
    z = z + 1

