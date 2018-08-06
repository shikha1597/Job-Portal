#!G:/Python27/python
#!/usr/bin/python

import cgi,cgitb
import MySQLdb
cgitb.enable()

print("Content-type:text/html\r\n\r\n")

print '<!DOCTYPE HTML>'
print '<!--'
print 'Aesthetic by gettemplates.co'
print 'Twitter: http://twitter.com/gettemplateco'
print 'URL: http://gettemplates.co'
print '-->'
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print '<title>Cube &mdash; Free Website Template, Free HTML5 Template by gettemplates.co</title>'
print '<meta name="viewport" content="width=device-width, initial-scale=1">'
print '<meta name="description" content="Free HTML5 Website Template by gettemplates.co" />'
print '<meta name="keywords" content="free website templates, free html5, free template, free bootstrap, free website template, html5, css3, mobile first, responsive" />'
print '<meta name="author" content="gettemplates.co" />'

print '<!-- Facebook and Twitter integration -->'
print '<meta property="og:title" content=""/>'
print '<meta property="og:image" content=""/>'
print '<meta property="og:url" content=""/>'
print '<meta property="og:site_name" content=""/>'
print '<meta property="og:description" content=""/>'
print '<meta name="twitter:title" content="" />'
print '<meta name="twitter:image" content="" />'
print '<meta name="twitter:url" content="" />'
print '<meta name="twitter:card" content="" />'

print '<link href="https://fonts.googleapis.com/css?family=Raleway:100,300,400,700" rel="stylesheet">'

print '<!-- Animate.css -->'
print '<link rel="stylesheet" href="css/animate.css">'
print '<!-- Icomoon Icon Fonts-->'
print '<link rel="stylesheet" href="css/icomoon.css">'
print '<!-- Themify Icons-->'
print '<link rel="stylesheet" href="css/themify-icons.css">'
print '<!-- Bootstrap  -->'
print '<link rel="stylesheet" href="css/bootstrap.css">'
print'<!-- Magnific Popup -->'
print'<link rel="stylesheet" href="css/magnific-popup.css">'

print'<!-- Owl Carousel  -->'
print'<link rel="stylesheet" href="css/owl.carousel.min.css">'
print'<link rel="stylesheet" href="css/owl.theme.default.min.css">'

print'<!-- Theme style  -->'
print'<link rel="stylesheet" href="css/style.css">'
print '<!-- Modernizr JS -->'
print '<script src="js/modernizr-2.6.2.min.js"></script>'
print '<!-- FOR IE9 below -->'
print '<!--[if lt IE 9]>'
print '<script src="js/respond.min.js"></script>'
print '<![endif]-->'

######################################################################################################
print '<body>'

print '<div class="gtco-loader"></div>'

print '<div id="page">'

print '<nav class="gtco-nav" role="navigation">'
print '<div class="gtco-container">'

print '<div class="row">'
print '<div class="col-sm-2 col-xs-12">'
##print '<div id="gtco-logo"><a href="index.html"><img src="images/logo.png" alt="Free HTML5 Website Template by GetTemplates.co"></a></div>'
print '</div>'
print '<div class="col-xs-10 text-right menu-1">'
print '<ul>'
print'<form action="">'
f=cgi.FieldStorage()
t1=int(f.getvalue("L1"))
try:
	db=MySQLdb.connect("127.0.0.1","root","","dbjobportal")
	c=db.cursor()
	sql="select * from student where s_id=%d"%(t1)
	
	try:
		c.execute(sql)
		resultset=c.fetchall()
		for row in resultset:
			name=row[0]
		print "<input type='text' name='L1' value=",name," readonly />"
	except Exception as e:
		print e
except Exception as e:
	print e		

print '<li><input type="submit" value="My Account" formaction="MyAccountJobSeeker.py"/>'
print '<input type="submit" value="Jobs" formaction="jobs.py"/>'
print '<li ><input type="submit" value="Update" formaction="updateCompanyDetail.py"></li>'
print '<li ><input type="submit" value="Delete Account" formaction="DeleteCompany.py"></a></li>'
print '<li ><input type="submit" value="Logout" formaction="index.html" /></li>'
print '</form>'
print '</ul>'
print '</div>'
print '</div>'
print '</div>'
print '</nav>'

#######################################################################################################
print '<header id="gtco-header" class="gtco-cover gtco-cover-xs gtco-inner" role="banner">'
print '<div class="gtco-container">'
print '<div class="row">'
print '<div class="col-md-12 col-md-offset-0 text-left">'
print '<div class="display-t">'
print '<div class="display-tc">'
print '<div class="row">'
print '<div class="col-md-8" style="width: 90em;overflow-x: auto;white-space: nowrap;">'

#######################################################################################################
print '<center><h2><u>Editing Personal Details</u></h2></center>'

try:
	db=MySQLdb.connect("127.0.0.1","root","","dbjobportal")
	c=db.cursor()
	sql="select * from student where s_id=%d"%(t1)
	try:	
		c.execute(sql)
		resultset=c.fetchall()
		print "<table>"
		print "<tr align='center'><td><input type='text' value='ID' readonly /></td>"
		print "<td ><input type='text' value='Name' readonly /></td> "
		print "<td><input type='text' value='Email' readonly /></td> "
		print "<td><input type='text' value='Phone Number' readonly /></td>"
		print "<td><input type='text' value='Course' readonly /></td>"
		print "<td><input type='text' value='Secondary School' readonly /></td>"
		print "<td><input type='text' value='Marks(10th)' readonly /></td>"
		print "<td><input type='text' value='Sr. Secondary School' readonly /></td>"
		print "<td><input type='text' value='Marks(12th)' readonly /></td>"
		print "<td><input type='text' value='College' readonly /></td>"
		print "<td><input type='text' value='Graduation Marks' readonly /></td>"
		print "<td><input type='text' value='Experience' readonly /></td>"
		print "<td><input type='text' value='Password' readonly /></td></tr></table>"
			
		for row in resultset:
			id=row[0]
			n=row[1]
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
				
			print "<form action='updateStudentDetail1.py' method='post'>"
			print("<table>")
			print "<tr><td><input type='text' name='t11' value=%d"%(id)+" required  readonly/></td>"
			print "<td><input type='text' name='t12' value='"+n+"' required /></td>"
			print "<td><input type='email' name='t13' value='"+em+"' required /></td>"
			print "<td><input type='text' name='t14' value='"+c+"' required /></td>"
			print "<td><input type='number' name='t15' value=",c_id," required readonly /></td>"
			print "<td><input type='text' name='t16' value='"+s_t1+"' required /></td>"
			print "<td><input type='text' name='t17' value=",t1," required /></td>"
			print "<td><input type='text' name='t18' value='"+s_t2+"' required /></td>"		
			print "<td><input type='number' name='t19' value=",t2," required /></td>"
			print "<td><input type='text' name='t20' value='"+s_t3+"' required /></td>"
			print "<td><input type='number' name='t21' value=",t3," required /></td>"
			print "<td><input type='number' name='t22' value=",e," required /></td>"
			print "<td><input type='text' name='t23' value='"+p+"' required /></td></tr></table>"
			print"<br/><br/>"
			print "<center><input type='submit' value='Update Details' name='b1'></center>"
			print"</form>"
	except Exception as e:
			print(e)
	finally:
			db.close()
			
except Exception as e:
		print(e)
		
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</header>'
print '<!-- END #gtco-header -->'
#######################################################################################################

#############################################################################################################

#####################################################################################3
print'<div class="gtco-section gtco-testimonial gtco-gray">'
print'<div class="gtco-container">'

print'<div class="row row-pb-sm">'
print'<div class="col-md-8 col-md-offset-2 gtco-heading text-center">'
print '<h2>People Love Us</h2>'
print '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus placerat enim et urna sagittis, rhoncus euismod erat tincidunt. Donec tincidunt volutpat erat.</p>'
print'</div>'
print '</div>'
print '<div class="row">'
print '<div class="col-md-6 col-sm-6 animate-box">'
print '<div class="gtco-testimony gtco-left">'
print '<div><img src="images/person_3.jpg" alt="Free Website template by GetTemplates.co"></div>'
print '<blockquote>'
print '<p>&ldquo;I think design would be better if designers were much more skeptical about its applications. If you believe in the potency of your craft, where you choose to dole it out is not something to take lightly.&rdquo; <cite class="author">&mdash; Frank Chimero</cite></p>'
print '</blockquote>'	
print '</div>'
print '</div>'

print '<div class="col-md-6 col-sm-6 animate-box">'
print '<div class="gtco-testimony gtco-left">'
print '<div><img src="images/person_1.jpg" alt="Free Website template by GetTemplates.co"></div>'
print '<blockquote>'
print '<p>&ldquo;Design must be functional and functionality must be translated into visual aesthetics, without any reliance on gimmicks that have to be explained.&rdquo; <cite class="author">&mdash; Ferdinand A. Porsche</cite></p>'
print '</blockquote>'	
print '</div>'
print '</div>'
print '</div>'

print '<div class="row">'
print '<div class="col-md-6 col-sm-6 animate-box">'
print '<div class="gtco-testimony gtco-left">'
print '<div><img src="images/person_3.jpg" alt="Free Website template by GetTemplates.co"></div>'
print '<blockquote>'
print '<p>&ldquo;I think design would be better if designers were much more skeptical about its applications. If you believe in the potency of your craft, where you choose to dole it out is not something to take lightly.&rdquo; <cite class="author">&mdash; Frank Chimero</cite></p>'
print '</blockquote>'	
print '</div>'
print '</div>'

print '<div class="col-md-6 col-sm-6 animate-box">'
print '<div class="gtco-testimony gtco-left">'
print '<div><img src="images/person_1.jpg" alt="Free Website template by GetTemplates.co"></div>'
print '<blockquote>'
print '<p>&ldquo;Design must be functional and functionality must be translated into visual aesthetics, without any reliance on gimmicks that have to be explained.&rdquo; <cite class="author">&mdash; Ferdinand A. Porsche</cite></p>'
print '</blockquote>'	
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</div>'



###########################################################################################
print '<footer id="gtco-footer" class="gtco-section" role="contentinfo">'
print '<div class="gtco-container">'
print '<div class="row row-pb-md">'
print '<div class="col-md-8 col-md-offset-2 gtco-cta text-center">'
print '<h3>We Love To Talk About Your Business</h3>'
print '<p><a href="#" class="btn btn-white btn-outline">Contact Us</a></p>'
print '</div>'
print '</div>'
print '<div class="row row-pb-md">'
print '<div class="col-md-4 gtco-widget gtco-footer-paragraph">'
print '<h3>Cube</h3>'
print '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus placerat enim et urna sagittis, rhoncus euismod.</p>'
print '</div>'
print '<div class="col-md-4 gtco-footer-link">'
print '<div class="row">'
print '<div class="col-md-6">'
print '<ul class="gtco-list-link">'
print '<li><a href="#">Home</a></li>'
print '<li><a href="#">Features</a></li>'
print '<li><a href="#">Products</a></li>'
print '<li><a href="#">Testimonial</a></li>'
print '<li><a href="#">Contact</a></li>'
print '</ul>'
print '</div>'
print '<div class="col-md-6">'
print '<p>'
print '<a href="tel://1234567890">+1 234 4565 2342</a> <br>'
print '<a href="#">info@domain.com</a>'
print '</p>'
print '</div>'
print '</div>'
print '</div>'
print '<div class="col-md-4 gtco-footer-subscribe">'
print '<form class="form-inline">'
print '<div class="form-group">'
print '<label class="sr-only" for="exampleInputEmail3">Email address</label>'
print '<input type="email" class="form-control" id="" placeholder="Email">'
print '</div>'
print '<button type="submit" class="btn btn-primary">Send</button>'
print '</form>'
print '</div>'
print '</div>'
print '</div>'
print '<div class="gtco-copyright">'
print '<div class="gtco-container">'
print '<div class="row">'
print '<div class="col-md-6 text-left">'
print '<p><small>&copy; 2016 Free HTML5. All Rights Reserved. </small></p>'
print '</div>'
print '<div class="col-md-6 text-right">'
print '<p><small>Designed by <a href="http://gettemplates.co/" target="_blank">GetTemplates.co</a> Demo Images: <a href="http://pixeden.com/" target="_blank">Pixeden</a> &amp; <a href="http://unsplash.com" target="_blank">Unsplash</a></small> </p>'
print '</div>'
print '</div>'
print '</div>'
print '</div>'
print '</footer>'

print '</div>'

print '<div class="gototop js-top">'
print '<a href="#" class="js-gotop"><i class="icon-arrow-up"></i></a>'
print '</div>'

print '<!-- jQuery -->'
print '<script src="js/jquery.min.js"></script>'
print '<!-- jQuery Easing -->'
print '<script src="js/jquery.easing.1.3.js"></script>'
print '<!-- Bootstrap -->'
print '<script src="js/bootstrap.min.js"></script>'
print '<!-- Waypoints -->'
print '<script src="js/jquery.waypoints.min.js"></script>'
print '<!-- countTo -->'
print '<script src="js/jquery.countTo.js"></script>'
print '<!-- Carousel -->'
print '<script src="js/owl.carousel.min.js"></script>'
print '<!-- Magnific Popup -->'
print '<script src="js/jquery.magnific-popup.min.js"></script>'
print '<script src="js/magnific-popup-options.js"></script>'



print '<!-- Main -->'
print '<script src="js/main.js"></script>'
print '</body>'
print '</html>'

