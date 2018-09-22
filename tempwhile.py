import random
while True:
	a=input("press 'r' to roll a dice,'q'to quit")	
	if(a=='r'):
		print("rolling dice.....")
		t=random.randint(1,6)
		print(t)
	else:
		print("BYE:):)")
		break
