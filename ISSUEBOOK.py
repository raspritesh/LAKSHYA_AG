import time
import MySQLdb as m

#variable to tell sql to what need to be done

def issue():
	#connector for mysql 
	db=m.connect("localhost","root","ritesh","cap")

#variable to tell sql to what need to be done

	sql="""CREATE TABLE IF NOT EXISTS d(id varchar(10) not null,name varchar(20) not null,bookid varchar(10) not null,bookname varchar(30) 		not null,issuedate varchar(10),returndate varchar(10),status varchar(5))"""
	cur=db.cursor()
	cur.execute(sql)

	st=0
	#res=rfidreader1.reading()
	#print res
	res=raw_input("Enter bookid")
	sql="select status from d where bookid='%s';" %res
	cur.execute(sql)
	result=cur.fetchall()
	for i in result:
		st=i[0]
        
        
	if res!=None and st=='1':
		print "Book already Issued"
		
		
		
	elif res!=None:
        	        
		inp1=raw_input("Enter ID").strip('\n')
        	inp2=raw_input("Enter name").strip('\n')
        	inp3=raw_input("Enter bookname").strip('\n')
        	inp4=raw_input("Enter issuedate").strip('\n')  # for eg. 22/07/2017
        	inp5=raw_input("Enter return date").strip('\n')
        	inp6=1
        	print "Book Issued successfully"
        	sql="insert into d(id,name,bookid,bookname,issuedate,returndate,status) values('%s','%s','%s','%s','%s','%s','%s');"%(inp1,inp2,res,inp3,inp4,inp5,inp6)
		try:
                	
			cur.execute(sql)
                	db.commit()
			
		except Exception as e:
                	print "Some error occured:",e
                	db.rollback()

                
	time.sleep(1)	
