import math
lst=[0.35,0.30,0.20,0.10,0.04,0.005,0.005]# INPUT YOUR VALUES HERE BEFORE RUNNING THE CODE
j=2 #CODING SYMBOL CAN BE CHANGED AND CAN BE USED TO IMRPOVE EFFCIENCY  
n=0

def _suminfo(x):
   sum=0
   for i in x:
       sum = sum + i
   return(1/sum)

def _sumentro(x):
   sum=0
   for i in x:
      sum = sum + i*(math.log(1/i,2))
   return(sum)

if(len(lst)/2==0):
    n=math.log(len(lst),2)
    nim=j*(math.log(len(lst),2))
else:
    n=math.log(len(lst),2)+1
    nim=j*(math.log(len(lst),2))+1

added =_suminfo(lst)
infor = math.log(added,2)
entro = _sumentro(lst)
print('Information rate is = ',infor)
print('Entropy  = ',entro,'bits/msg')
print('efficiency =',(entro/n)*100,'% n =',n,)
print('improved coding n value =',nim,'with val of j =',j,'and new efficiency =',(j*entro/nim)*100,'%')
