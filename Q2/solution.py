N = int(input())
lines = []

for i in range(N):
    lines.append(input())

allValid =True
errorCodes = []

for line in lines:
    if "false" in line:
        allValid = False
        f_posi = line.find("false")
        errorCodes.append(line[(f_posi+6):])
    

if allValid==True:
    print("Yes")
    print(errorCodes)
else:
    print("No")
    print(' '.join(errorCodes))