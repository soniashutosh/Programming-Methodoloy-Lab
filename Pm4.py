#Assumptions: 
#1.Only few variables are allowed
#2.Read from file and output on Terminal





import sys
char=['a','b','c','d']
sign=['+','-','*','/']
f=open("New.txt","r")
line1=f.readline()
if line1!="Begin\n":
	print("Starting not found")
	sys.exit()
sta=f.readline()
a=1
while sta!='End\n':
	flag=0
	new=[];
	li=list(sta)
	size=len(li)
	count=1
	if li[size-2]==";":
		#print("Ending of line {0} not Exist".format(a))
		for i in char:
			if li[0]==i:
				if li[1]=="=":
					count=0
					#print("heyy")
					break
	#print(count)
	if count==0:
		for i in char:
			if li[2]==i:
				count=1
	else:
		print("Invalid Syantax")
		flag=1
	if count==1 and flag==0:
		i=3
		left=0
		right=0
		make=0
		while i<(size-3):
			for j in sign:
				if li[i]==j:
					if li[i]=="*"and li[i+1]=="*":
						for k in char:
							if li[i+2]==k:
								right=1;
						for k in char:
							if li[i-1]==k:
								left=1;
						if right==1 and left==1:
							print(" ..**{0} is correct".format(li[i+2]))
							i+=3
							break
						else:
							print("Invalid Syantax of **")
							i+=3
							flag=1
					else:
						for k in char:
							if li[i+1]==k:
								make=1;
						if make==1:
							print("{0}{1}... is correct".format(li[i-1],li[i]))
							i+=2;
							break
						else:
							print("Invalid Syantax of {0}".format(li[i]))
							i+=2;
							flag=1
	if flag==0:
		print("Line {0} is correct".format(a))
	else:
		print("Line {0} is incorrect".format(a))
	sta=f.readline()
	#print(sta)
	a+=1
f.close()