#!G:/Python27/python
#!/usr/bin/python
import cgi,cgitb
import MySQLdb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")

print'<!DOCTYPE HTML>'
print'<!--'
print'Aesthetic by gettemplates.co'
print'Twitter: http://twitter.com/gettemplateco'
print'URL: http://gettemplates.co'
print'-->'
print'<html>'
print'<head>'
print'<meta charset="utf-8">'
print'<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print'<title>Cube &mdash; Free Website Template, Free HTML5 Template by gettemplates.co</title>'
print'<meta name="viewport" content="width=device-width, initial-scale=1">'
print'<meta name="description" content="Free HTML5 Website Template by gettemplates.co" />'
print'<meta name="keywords" content="free website templates, free html5, free template, free bootstrap, free website template, html5, css3, mobile first, responsive" />'
print'<meta name="author" content="gettemplates.co" />'

print'<!-- Facebook and Twitter integration -->'
print'<meta property="og:title" content=""/>'
print'<meta property="og:image" content=""/>'
print'<meta property="og:url" content=""/>'
print'<meta property="og:site_name" content=""/>'
print'<meta property="og:description" content=""/>'
print'<meta name="twitter:title" content="" />'
print'<meta name="twitter:image" content="" />'
print'<meta name="twitter:url" content="" />'
print'<meta name="twitter:card" content="" />'

print'<link href="https://fonts.googleapis.com/css?family=Raleway:100,300,400,700" rel="stylesheet">'

print'<!-- Animate.css -->'
print'<link rel="stylesheet" href="css/animate.css">'
print'<!-- Icomoon Icon Fonts-->'
print'<link rel="stylesheet" href="css/icomoon.css">'
print'<!-- Themify Icons-->'
print'<link rel="stylesheet" href="css/themify-icons.css">'
print'<!-- Bootstrap  -->'
print'<link rel="stylesheet" href="css/bootstrap.css">'

print'<!-- Magnific Popup -->'
print'<link rel="stylesheet" href="css/magnific-popup.css">'

print'<!-- Owl Carousel  -->'
print'<link rel="stylesheet" href="css/owl.carousel.min.css">'
print'<link rel="stylesheet" href="css/owl.theme.default.min.css">'

print'<!-- Theme style  -->'
print'<link rel="stylesheet" href="css/style.css">'

print'<!-- Modernizr JS -->'
print'<script src="js/modernizr-2.6.2.min.js"></script>'
print'<!-- FOR IE9 below -->'
print'<!--[if lt IE 9]>'
print'<script src="js/respond.min.js"></script>'
print'<![endif]-->'

print'</head>'
print'<body>'

print'<div class="gtco-loader"></div>'

print'<div id="page">'

print'<nav class="gtco-nav" role="navigation">'
print'<div class="gtco-container">'

print'<div class="row">'
print'<div class="col-sm-2 col-xs-12">'
print'<div id="gtco-logo"><a href="index.html"><img src="images/logo.png" alt="Free HTML5 Website Template by GetTemplates.co"></a></div>'
print'</div>'
print'<div class="col-xs-10 text-right menu-1">'
print'<ul>'
print'<form>'
f=cgi.FieldStorage()
L1=int(f.getvalue("L1"))
db=MySQLdb.connect("127.0.0.1","root","","dbjobportal")
c=db.cursor()
print "<input type='text' name='L1' value=",L1," readonly />"


print '<li><input type="submit" value="My Account" formaction="MyAccountCompany.py"/>'

print '<li><input type="submit" value="View Vacancies" formaction="ShowVacancy.py"/>'
print "<li><input type='submit' value='Add Vacancies' formaction='AddVacancy.py>'</li>"
print "<li><input type='submit' value='Update/Delete Vacancy' formaction='UpdateVacancyDetail.py'><li>"
print '<li ><input type="submit" value="Update" formaction="updateCompanyDetail.py"></li>'
print '<li ><input type="submit" value="Delete Account" formaction="DeleteCompany.py"></a></li>'
print '<li ><input type="submit" value="Logout" formaction="index.html" /></li>'
print '</form>'

print'</ul>'
print'</div>'
print'</div>'

print'</div>'
print'</nav>'

print'<header id="gtco-header" class="gtco-cover gtco-cover-xs gtco-inner" role="banner">'
print'<div class="gtco-container">'
print'<div class="row">'
print'<div class="col-md-12 col-md-offset-0 text-left">'
print'<div class="display-t">'
print'<div class="display-tc">'
print'<div class="row">'
print'<div class="col-md-8">'
print'<h1 class="no-margin">Add Vacancy</h1>'
print'</div>'
print'</div>'
print'</div>'
print'</div>'
print'</div>'
print'</div>'
print'</div>'
print'</header>'
print'<!-- END #gtco-header -->'



print'<div class="gtco-section">'
print'<div class="gtco-container">'
print'<div class="row">'
print'<div class="col-md-8 col-md-offset-2 gtco-heading text-center">'
print'</div>'
print'</div>'
print'<div class="row">'
print'<div class="col-md-6">'
print'<form action="AddVacancy2.py">'
print'<div class="form-group">'
print'<label for="name">Company id</label>'#COMPANY ID
print'<input type="text" class="form-control" id="name" value=%d'%(L1)+' name="t1" required />'
print'</div>'
print'<div class="form-group">'
print'<label for="name">Department</label>'
sql2='select * from department'
try:
	c.execute(sql2)
	resultset=c.fetchall()
	print "<select class='form-control' name='Department'>"
	print"<option value='0' selected></option>"
	for row in resultset:
		id=row[0]
		name=row[1]
		print "<option value='",id,"'>"+name+"</option>"
	print"</select>"
except Exception as e:
	print e
print'</div>'
print'<div class="form-group">'
print'<label for="name">Degree Required</label>'
sql1='select * from course'
try:
	c.execute(sql1)
	resultset=c.fetchall()
	print "<select class='form-control' name='Course'>"
	print"<option value='0' selected></option>"
	for row in resultset:
		id=row[0]
		name=row[1]
		print "<option value='",id,"'>"+name+"</option>"
	print"</select>"
except Exception as e:
	print e
print'</div>'
print'<div class="form-group">'
print'<label for="name">Post Name</label></br>'
print'<input type="text" class="form-control" name="t2" required />' 

print'</div>'

print'<div class="form-group">'
print'<label for="name">Number of Vacancies</label>'
print'<input type="number" class="form-control" id="tenth_marks" name="t3" required />'
print'</div>'
print'<div class="form-group">'
print'<label for="name">Salary(per month)</label>'
print'<input type="number" class="form-control" id="sal" name="t4" required />'
print'</div>'
print'<div class="form-group">'
print'<label for="name">Required 10th marks</label>'
print'<input type="number" class="form-control" id="tenth_marks" name="t5" required />'
print'</div>'

print'<div class="form-group">'
print'<label for="name">Required 12th marks</label>'
print'<input type="number" class="form-control" id="twelth_marks" name="t6" required />'
print'</div>'
print'<div class="form-group">'
print'<label for="name">Required Graduation marks</label>'
print'<input type="number" class="form-control" id="tenth_marks" name="t7" required />'
print'</div>'
print'<div class="form-group">'
print'<label for="name">Experience</label>'
print'<input type="number" class="form-control" id="experience" name="t8" required />'
print'</div>'


print'<div class="form-group">'
print'<input type="submit" class="btn btn btn-special" value="Add Vacancy">'
print'</div>'
print'</form>'
print'</div>'

print'</div>'
print'</div>'
print'</div>'
print'<!-- END .gtco-services -->'





print'<footer id="gtco-footer" class="gtco-section" role="contentinfo">'
print'<div class="gtco-container">'
print'<div class="row row-pb-md">'
print'<div class="col-md-8 col-md-offset-2 gtco-cta text-center">'
print'<h3>We Love To Talk About Your Business</h3>'
print'<p><a href="#" class="btn btn-white btn-outline">Contact Us</a></p>'
print'</div>'
print'</div>'
print'<div class="row row-pb-md">'
print'<div class="col-md-4 gtco-widget gtco-footer-paragraph">'
print'<h3>Cube</h3>'
print'<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus placerat enim et urna sagittis, rhoncus euismod.</p>'
print'</div>'
print'<div class="col-md-4 gtco-footer-link">'
print'<div class="row">'
print'<div class="col-md-6">'
print'<ul class="gtco-list-link">'
print'<li><a href="#">Home</a></li>'
print'<li><a href="#">Features</a></li>'
print'<li><a href="#">Products</a></li>'
print'<li><a href="#">Testimonial</a></li>'
print'<li><a href="#">Contact</a></li>'
print'</ul>'
print'</div>'
print'<div class="col-md-6">'
print'<p>'
print'<a href="tel://1234567890">+1 234 4565 2342</a> <br>'
print'<a href="#">info@domain.com</a>'
print'</p>'
print'</div>'
print'</div>'
print'</div>'
print'<div class="col-md-4 gtco-footer-subscribe">'
print'<form class="form-inline">'
print'<div class="form-group">'
print'<label class="sr-only" for="exampleInputEmail3">Email address</label>'
print'<input type="email" class="form-control" id="" placeholder="Email">'
print'</div>'
print'<button type="submit" class="btn btn-primary">Send</button>'
print'</form>'
print'</div>'
print'</div>'
print'</div>'
print'<div class="gtco-copyright">'
print'<div class="gtco-container">'
print'<div class="row">'
print'<div class="col-md-6 text-left">'
print'<p><small>&copy; 2016 Free HTML5. All Rights Reserved. </small></p>'
print'</div>'
print'<div class="col-md-6 text-right">'
print'<p><small>Designed by <a href="http://gettemplates.co/" target="_blank">GetTemplates.co</a> Demo Images: <a href="http://pixeden.com/" target="_blank">Pixeden</a> &amp; <a href="http://unsplash.com" target="_blank">Unsplash</a></small> </p>'
print'</div>'
print'</div>'
print'</div>'
print'</div>'
print'</footer>'

print'</div>'

print'<div class="gototop js-top">'
print'<a href="#" class="js-gotop"><i class="icon-arrow-up"></i></a>'
print'</div>'

print'<!-- jQuery -->'
print'<script src="js/jquery.min.js"></script>'
print'<!-- jQuery Easing -->'
print'<script src="js/jquery.easing.1.3.js"></script>'
print'<!-- Bootstrap -->'
print'<script src="js/bootstrap.min.js"></script>'
print'<!-- Waypoints -->'
print'<script src="js/jquery.waypoints.min.js"></script>'
print'<!-- Carousel -->'
print'<script src="js/owl.carousel.min.js"></script>'
print'<!-- Magnific Popup -->'
print'<script src="js/jquery.magnific-popup.min.js"></script>'
print'<script src="js/magnific-popup-options.js"></script>'

print'<!-- Google Map -->'
print'<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA&sensor=false"></script>'
print'<script src="js/google_map.js"></script>'

print'<!-- Main -->'
print'<script src="js/main.js"></script>'

print'</body>'
print'</html>'

