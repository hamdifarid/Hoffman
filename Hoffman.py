import math
InputNum = []
NumVar = int(input("Number of variables:"))

for i in range(0,NumVar):
    print("Enter value for (",i,"):")
    InpX = float(input())
    InputNum.append(InpX)

#Check if the numbers are same in Array
for i in range(0,NumVar-1):
    if (InputNum[i] == InputNum[i+1]):
        InputNum[i+1] += 0.0000000001

InputNum.sort(reverse=True)

Numbers = []
TempArray = InputNum.copy()
EntroArrau = InputNum.copy()
sumn=0
sumentro=0

def _sumentro(x):
   sum=0
   for i in x:
      sum = sum + i*(math.log(1/i,2))
   return(sum)


sumentro=_sumentro(EntroArrau)

for x in range(0,NumVar):
    InputNum = TempArray.copy()
    Numbers.append("")
    ValueOf = InputNum[x]
    for i in range(NumVar-1,0,-1):
        v1 = InputNum[i]
        v2 = InputNum[i-1]
        v3 = v1 + v2 + 0.00000000001
        if (v2 == ValueOf):
            Numbers[x] = "0" + Numbers[x]
            ValueOf = v3
        if (v1 == ValueOf):
            Numbers[x] = "1" + Numbers[x]
            ValueOf = v3
        #print(InputNum," - ",Numbers[x])
        InputNum.pop(i)
        InputNum.pop(i-1)
        vx = v3
        InputNum.append(vx)
        InputNum.sort(reverse=True)
    print("Code word for ",TempArray[x]," is ",Numbers[x]," length of ",len(Numbers[x]))
    sumn=sumn+TempArray[x]*len(Numbers[x])
    
print("N =",sumn,'bit/msg',)
print("entropy H=",sumentro)
print("Code efficiency =",(sumentro/sumn)*100)   
