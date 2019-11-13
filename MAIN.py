import time
import ISSUEBOOK as i
import RETURNBOOK as r
import MySQLdb as m
while True:
	inp=0
	print("\t\t\t\t WELCOME TO LIBRARY MANAGEMENT SYSTEM\t\t\t\t\t\n")
	print("\t\t Developed by Lakshya Agarwal(Roll Number :35) and Lohit Bhardwaj (ROll Number : 38)\n")
	print("\t\t\t\t\t MENU \n")
	print("\t\t\t 1.ISSUE\n")
	print("\t\t\t 2.RETURN\n")
	print("\t\t\t 3.DISPLAY ACTIVE STATUS \n")
	print("\t\t\t 4.DISPLAY ALL Information \n")
	print("\t\t\t 5.Search By Roll Number \n")
	print("\t\t\t 6.Search By Book ID \n")
	print("\t\t\t 7.Exit\n")
	inp=int(input("Please Enter your choice : "))
	if inp == 1:
		i.issue()
	elif inp == 2 :
		r.return_book()
	elif inp == 3:
		db=m.connect("localhost","root","ritesh","cap")
		cur=db.cursor()
		sql="select * from d where status = '1';"
        	cur.execute(sql)
		result=cur.fetchall()
		if result==():
                	print "No active books found"
       		else:
            		for row in result:
				
	                    	Id=row[0]
	                    	name=row[1]
				bookname=row[2]	
                   		print "Registration Number='%s'"%Id,
           			print "Name='%s'"%name,
				print "Book Name='%s'"%bookname,	
				print ("\n")
	elif inp == 4:
		db=m.connect("localhost","root","ritesh","cap")
		cur=db.cursor()
		sql="select * from d ;"
        	cur.execute(sql)
		result=cur.fetchall()
            	for row in result:
				
	        	Id=row[0]
	                name=row[1]
			bookid=row[2]
			bookname=row[3]	
			issuedate=row[4]
               		status=int(row[6])
                   	print "Registration Number='%s'"%Id,
           		print "Name='%s'"%name,
			print "Book ID='%s'"%bookid,
			print "Book Name='%s'"%bookname,
			print "IssueDate='%s'"%issuedate,
			if status == 1:
				print("Book status : Not returned ")
			elif status == 0 :
				print("Book status : returned")	
	elif inp == 5 :
		db=m.connect("localhost","root","ritesh","cap")
		cur=db.cursor()
		roll_input=int(input("Enter Roll Number of student : "))
		sql="select * from d where id='%s';"%roll_input
		cur.execute(sql)
		result=cur.fetchall()
		if result==():
                	print "No student found"
        	else:
            		for row in result:
				
	        		Id=row[0]
	                	name=row[1]
				bookid=row[2]
				bookname=row[3]	
				issuedate=row[4]
				status=int(row[6])
                   		print "Registration Number='%s'"%Id,
           			print "Name='%s'"%name,
				print "Book ID='%s'"%bookid,
				print "Book Name='%s'"%bookname,
				print "IssueDate='%s'"%issuedate,
				if status == 1:
					print("Book status : Not returned ")
				elif status == 0 :
					print("Book status : returned")
	elif inp == 6 :
		db=m.connect("localhost","root","ritesh","cap")
		cur=db.cursor()
		bookid_input=int(input("Enter Book ID : "))
		sql="select * from d where bookid='%s';"%bookid_input
		cur.execute(sql)
		result=cur.fetchall()
		if result==():
                	print "No Book found"
        	else:
            		for row in result:
				
	        		Id=row[0]
	                	name=row[1]
				bookid=row[2]
				bookname=row[3]	
				issuedate=row[4]
				status=int(row[6])
                   		print "Registration Number='%s'"%Id,
           			print "Name='%s'"%name,
				print "Book ID='%s'"%bookid,
				print "Book Name='%s'"%bookname,
				print "IssueDate='%s'"%issuedate,
				if status == 1:
					print("Book status : Not returned ")
				elif status == 0 :
					print("Book status : returned")		
            			
	elif inp == 7: 
		print("Exit")
		break
	else : 
		print ("Enter Valid Input")

	print("\n\n\n\n")
