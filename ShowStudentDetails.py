#!G:/Python27/python
#!/usr/bin/python
import cgi,cgitb
import MySQLdb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
try:
	f=cgi.FieldStorage()
	email=((f.getvalue('t1')))
	pwd=f.getvalue('t2')
	try:
		db=MySQLdb.connect("127.0.0.1","root","","dbjobportal")
		c=db.cursor()
		sql="select student.s_id,name,student.email,student.contact,course.course_name, student.school_10,student.tenth_marks,student.school_12,student.twelth_marks,student.college,student.graduation_marks, student.experience,student.password from student,course where email='%s' and password='%s' and course.course_id=student.course_id"%(email,pwd)
		try:
			c.execute(sql)
			resultset=c.fetchall()
			for row in resultset:
				id=row[0]
				name=row[1]
				em=row[2]
				c=row[3]
				c_id=row[4]
				s_t1=row[5]
				t1=row[6]
				s_t2=row[7]
				t2=row[8]
				s_t3=row[9]
				t3=row[10]
				e=row[11]
				p=row[12]
				print "<label name='l1'>",id,"</label><br/>"
				print name+"<br/>"
				print em+"<br/>"
				print "Contact Number: "+c+"<br/>"
				print "Course: "+c_id+"<br/>"
				print "School(1oth): "+s_t1+"<br/>"
				print "10th Marks: ",t1,"<br/>"
				print "School(12th): "+s_t2+"<br/>"
				print "12th Marks: ",t2,"<br/>"
				print "College: "+s_t3+"<br/>"
				print "Graduation Marks: ",t3,"<br/>"
				print "Experience: ",e,"<br/>"
				print "Password: "+p+"<br/>"
				
		except Exception as e:
			print(e)
		finally:
			db.close()
		
	except Exception as e:
		print(e)
		
	print"<br/><br/>"	
	print "<form action='main.html'>"
	print "<input type='submit' value='Home' />"	
		
except ValueError:
		print("Enter valid Comapany id.")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		zz