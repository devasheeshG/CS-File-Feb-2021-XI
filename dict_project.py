def add_stud():
	rollno = int(input("Enter Roll number : "))
	name = input("Enter name : ")
	dt[rollno] = name
	
def disp_stud():
	print( "Roll no. \t name")
	for key in dt :
		print( key, "\t\t" , dt[key] ) 
	
def srch_stud():
		r = int(input("Enter roll number : "))
		if r in dt :
			print( "Roll no. \t name")
			print(r, "\t\t" , dt[r] )
		else :
			print("Student not found!!!")
		
def del_stud():
	r = int(input("Enter roll number : "))
	if r in dt :
		del dt[r]
		print("deleted successfully!!!")
	else :
		print("Student not found!!!")
		
		
		
dt = { }
while True :
	ch = int(input("\n * Main Menu * \n press 1 for add \n press 2 for display \n press 3 for search \n press 4 for delete \n press 9 for exit\n"))
	if ch == 1 :
		add_stud()
	elif ch == 2 :
		disp_stud()
	elif ch == 3 :
		srch_stud()
	elif ch == 4 :
		del_stud()
	
	elif ch == 9 :
		break