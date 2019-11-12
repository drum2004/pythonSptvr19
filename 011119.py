#01.11.19
#1--------------
a=1000
while a<=9999:
    print(a)
    a+=3
   
#2----------------------------
x=1
steps=0
while steps<=55:
    print('#',steps,'',x )
    x+=2
    steps+=1
#3--------------------------------
x=90
while x>=0:
    print(x)
    x-=5
#4-------------------------------
a=2
i=0
while i<=20:
    print(i,'',a)
    a*=2
    i+=1    
#5--------------------------------
a=2
while a<=10000:
    print(a)
    a=a*2-1
#6----------------------------------
a=-166
while a<100:
    if -100<a<-9 or 9<a<100:
        print(a)
    a=2*a+200   
#7-------------------------
n=int(input('n:'))
i=1
f=1
while i<=n:
    f*=i
    i+=1
print(f) 
#8----------------
n=int(input('n:'))
i=1
b=0

for i in range(1,999):
    if b==n%i:
        print(i)
#9-------------------
n=int(input('n:'))
i=1
b=0
for i in range(2,n):
    if i!=n and b==n%i:
        print(n,' -не простое число')
        break
    else:
        print(n,' -простое число')
        break
print('введеное число:',n)
#10-------------------------------
'''a1=3
a2=2
i=1
while i<=12:'''
a1=3
a2=2
for i in range(12):
    print('a1-',a1,'a2-',a2)
    a2 = a2*2-2;
    a1 = a1*2-2;
    
  









        