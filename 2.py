L = int(input())

A = []
num = ""

segment = 0

while (L > 0) :

    text = input()

    for letter in text:
        if letter in "1234567890":
         num = num + letter 
            
        else :
             A.append(num)
             A.append(letter)
             num = ""
    L = L - 1

for element in A:
    if '' in A:
        A.remove('')
    elif ' ' in A:
        A.remove(' ')
    
while segment < len(A):
    
    print(A[segment+1] * int(A[segment]) )

    segment = segment + 2


