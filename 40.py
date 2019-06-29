n=int(input())
p=0
q=1 
while(n>0):
   print(q,end=' ')
   p,q=q,p+q
   n-=1
