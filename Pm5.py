#Enter the Program

import sys

print("Enter Your Program")
num=input()
if(num!="Begin"):
	print("Wrong Format")
	sys.exit()

li=[]
sta=input()

while(sta!="1"):
	li.append(sta)
	sta=input()

num=len(li)

if(li[num-1]!="End"):
	print("Wrong Format")
	sys.exit()

print(num)

i=0
while(num-1):
	sta=li[i]
	cd=list(sta)
	if(i==0):
		

	i+=1
	num-=1
