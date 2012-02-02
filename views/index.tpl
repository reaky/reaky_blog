<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" /> 
		<title>Reaky yf</title>
		<link type="image/x-icon" href="/static/img/favicon.ico" rel="shortcut icon"/> 
		<link type="text/css" rel="stylesheet" href="/static/blog.css" media="screen" />
		<script type="text/javascript" src="/static/jquery-1.4.2.min.js"></script> 
		<script type="text/javascript" src="/static/jquery.form.js"></script> 
		<script type="text/javascript" src="/static/blog.js"></script>
	</head>
	<body><div id="main_page">
		<div id="navi_bar">
			<ul>
				<li><a id="navi_about" href="/about"><span>About</span></a></li>
				<li><a id="navi_buzz" href="/buzz"><span>Buzz</span></a></li>
				<li><a id="navi_blog" href="/blog"><span>Blog</span></a></li>
			</ul>
		</div>
		<div id="main_content">{% include "blog.html" %}</div>
		<div id="footer_bar">{% include "footer_bar.html" %}</div>
	</div></body>
</html>
