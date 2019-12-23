import sys 
char=['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numchar=['1','2','3','4','5','6','7','8','9','0','_','A','B','C','D','E','F','G',';','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sign=['+','-','*','/','=','(',')']
sign2=[')']


print("Enter 1 if you want to check the expression.....till then please input ...")
start=input()
if start!="Begin":
	print("Invalid Syantax")
	sys.exit()
li=[]
str1=input()
while str1!='1':
	li.append(str1)
	str1=input()

if li[-1]!="End":
	print("Invalid Syantax")
	print("End not exist")
	sys.exit()

random=0
count=len(li)
count1=0
i=0
li2=[]
while count-1:
	str1=li[i]
	li2=list(str1)
	count2=len(li2)
	for j in char:
		if li2[0]==j:
			count1+=1
	if count==0:
		print("Syantax Error in line {0}".format(i+1))
		random=1

	if li2[count2-1]!=';':
		print("Syanatx Error in line {0}".format(i+1))
		print("Ending of the statement is not proper")
		random=1

	k=1;
	while count2-2:
		count3=0
		for j in numchar:
			if li2[k]==j:
				count3+=1
				count2-=1
				k+=1
				break;
		if count3==0:
			for j in sign:
				if li2[k]==j:
					for m in sign:
						if li2[k+1]==m:
							for l in char:
								if li2[k+2]==l:
									count2-=3
									count3+=1
									k+=3
									break;
			if count3==0:
				for j in sign:
					if li2[k]==j:
						for l in char:
							if li2[k+1]==l:
								count2-=2
								count3+=1
								k+=2
								break;ew
		if count3==0:
			print("Syantax Error in line {0}".format(i+1))
			random=1
			break;
	i+=1
	count-=1
if random==0:
	print("Your Grammer is Alright ...")
