#Parking lot

slots=5
cars=[]
while True:
	print("1)Park car:")
	print("2)Remove car:")
	print("3)Check parking lot:")
	print("4)Exit:")
	ch=input("Choose:")
	if ch=="1":
		number=input("Enter the car number:")
		if number not in cars:
			if slots>0:
				cars.append(number)
				slots=slots-1
				print("Car parked!")
			else:
				print("Parking lot is full!")
		else:
			print("Car already exists!!")
	if ch=="2":
		number=input("Enter the car number:")
		if number in cars:
			cars.remove(number)
			slots=slots+1
			print("Car removed!")
		else:
			print("Car doesnt exist!")
	if ch=="3":
		if cars:
			print("Parked cars:",cars)
		else:
			print("Parking lot is empty!")
	if ch=="4":
		print("Thank you!")
		break
