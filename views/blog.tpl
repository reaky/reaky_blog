<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Reaky yf</title>
<link type="image/x-icon" href="/static/img/favicon.ico" rel="shortcut icon"/>
<link type="text/css" rel="stylesheet" href="/static/blog.css" media="screen" />
</head>
<body><div id="main_page">
<div id="navi_bar">
	<ul>
		<li><a id="navi_about" href="/about"><span>About</span></a></li>
		<li><a id="navi_GooglePlus" href="https://plus.google.com/104418721144979799988"><span>+Reaky</span></a></li>
		<li><a id="navi_blog" href="/"><span>Blog</span></a></li>
	</ul>
</div>
<div id="main_content">
%for article in posts:
<div class="article">
	<div class="article_key">{{ article[0] }}</div>
	<div class="article_title">{{ article[1] }}</div>
	<div class="article_time">{{ article[3][2:10] }}</div>
	<div class="article_content">{{ article[4] }}</div>
</div>
%end

<div id="article_comment">
<div id="comments_posted"></div><!--end comments_posted-->
<form id="comment_form" action="/addcomment/1" method="post">
<div>
	<input type="text" name="username" value="Name" />
	<input type="text" name="email" value="Email" />
	<input name="submit" type="submit" value="Submit" />
</div>
<textarea name="comment" rows="" cols="" value="要不留下点什么？"></textarea>
</form><!--end comment_form-->
</div><!--end article_comment-->
</div><!--end main_content-->
<div id="footer_bar">
	<span>
		<img src="/static/img/vi.powered.by.sven.gif" alt="Written in vim" title="Written in vim" />
		W3C 
		<a href=>HTML</a>&amp;
		<a href=>CSS</a>
		valid.
		UTF-8 encoded.
	</span><br />
	<span>© 2008 reaky All rights reserved, all wrongs observed.</span><br />
	<span>Powered by Python Bottle jQuery on iPad2</span>
</div><!--end footer_bar-->
</div><!--end main_page-->
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<!--<script type="text/javascript" src="/static/jquery-1.4.2.min.js"></script>-->
<script type="text/javascript" src="/static/jquery.form.js"></script>
<script type="text/javascript" src="/static/blog.js"></script>
<!--the start of the google analytics code-->
<script type="text/javascript">
	var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
	document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
	try {
		var pageTracker = _gat._getTracker("UA-15130903-1");
		pageTracker._trackPageview();
	} catch(err) {}</script>
<!--the end of the google analytics code-->
</body>
</html>