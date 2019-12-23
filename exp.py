#Beign the input in correct manner

#Assumptions
#1.Only One function can be defined
#2.As many loops can be used inside function
#3.Expressions Except Loop starting Ending and the Function syatax can be checked not the expressions inside the function

import sys

char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numchar=['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G',';','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def check( name ):
	an=list(name)
	count=0
	for i in char:
		if an[0]==i:
			count=1
	j=1
	for j in range(len(an)):
		si=0
		for k in numchar:
			if an[j]==k:
				si=1
		if si==0:
			return 0

	if count==1:
		return 1
	else:
		return 0

f=open("test.txt")

#line by libne list formed
count=0
li=[]   
sta=f.readline()
while sta!="End\n":
        li.append(sta)
        sta=f.readline()
        count+=1
        if count>20:
                print("End not exist")
                sys.exit()
count-=1

#checking function first line
sta=li[0]
li2=list(sta)
if sta[0:5]!="Begin":
        print("Invalid Input..Not started with Begin")
        sys.exit()

if(li2[5]!=" "):
        print("Not differenciable between Begin and function name")
        sys.exit()

ind=6
#print(li2)
name=[]
while li2[ind]!='_':
        name.append(li2[ind])
        ind+=1
        if ind==len(li2):
                print("Function definition is not correct")
                sys.exit()
ind+=1 
funname=""
for i in name:
        funname+=i
print("Function name is:",funname)
if check(funname)!=1:
	print("Wrong function name")
	sys.exit()

name.clear()
while li2[ind]!='_':
        name.append(li2[ind])
        ind+=1
        if ind==len(li2):
                print("Function definition is not correct")
                sys.exit()
ind+=1
varname="" 
vana=[]
for i in name:
        if i==' ':
                vana.append(varname)
                varname=""
        else:
                varname+=i
vana.append(varname)
varname=""

for ashu in vana:
	if check(ashu)!=1:
		print("Wrong function name")
		sys.exit()

print("Function variables are:",vana)            
 
if li2[ind]!=':':
        print("Function definition is not correct")
        sys.exit()

if (ind+2)!=len(li2):
        print("Invalid Syantax")   
        
#print("line 1 is correct")

#line 1 is checked

#Loop checking
varchecked=0
j=1
check=0 
while count:
        sta=li[j]
        li2=[]
        li2=list(sta)
        li3=[]
        name=""
        for i in li2:
                if i==' ' or i=='_' or i=='*' or i=='=' or i==';':
                        li3.append(name)
                        name=""
                        li3.append(i)
                else:
                        name+=i
        li3.append(name)
        #print(li2)
        #print(li3)  
        if li3[0]=="Loop":
                check=1
                #print("Loop started in line ",j)
                if li3[1]!='_':
                        print("Invalid syantax of loop")
                        sys.exit()
                if li3[3]!='_':
                        print("Invalid syantax of loop")
                        sys.exit()
                if li3[4]!="times:\n":
                        print("Invalid syantax of loop")
                        sys.exit()
                #print("Loop Starting Syantax is correct" )         
             
        if li3[0]=="Endloop\n":
                if check==0:
                        print("Loop Ending without starting...Error")
                        sys.exit()
                #else:
                       #print("Loop End in line ",j)  
                check=0     
        count-=1
        j+=1  
        for a in li3:
                for k in vana:
                        if a==k:
                                varchecked+=1

if varchecked<len(vana):
                print("Variables passes throgh the function is not used atleast once inside the function")   

if check==1:
        print("Loop Ending not takes place")     
        sys.exit()               

print("Program for One Function and for as many loop is validated and it is correct")

