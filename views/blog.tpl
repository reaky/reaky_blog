<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Reaky yf</title>
<link type="image/x-icon" href="/static/img/favicon.ico" rel="shortcut icon"/>
<link type="text/css" rel="stylesheet" href="/static/blog.css" media="screen" />
</head>
<body>
<header><nav>
	<ul>
		<li><a id="navi_about" href="/about"><span>About</span></a></li>
		<li><a id="navi_GooglePlus" href="https://plus.google.com/104418721144979799988"><span>+Reaky</span></a></li>
		<li><a id="navi_github" href="https://github.com/reaky">GitHub</a></li>
		<li><a id="navi_blog" href="/"><span>Blog</span></a></li>
	</ul>
</nav></header>
<section id="main_content">
%for article in posts:
<article>
	<div class="article_key">{{ article[0] }}</div>
	<div class="article_title">{{ article[1] }}</div>
	<div class="article_time">{{ article[3][2:10] }}</div>
	<div class="article_content">{{ article[4] }}</div>
</article>
%end

<section id="article_comment">
<div id="comments_posted"></div><!--end comments_posted-->
<form id="comment_form" action="/addcomment/1" method="post">
	<input id="comment_user" type="text" name="username" size="26" value="Name" tabindex="1" />
	<input id="comment_email" type="text" name="email" size="26" value="Email" tabindex="2" />
	<input id="comment_submit" name="submit" type="submit" value="Submit" tabindex="4" />
	<textarea id="comment_content" name="comment" rows="6" cols="80" value="要不留下点什么？" tabindex="3"></textarea>
</form><!--end comment_form-->
</section><!--end article_comment-->
</section><!--end main_content-->
<footer>
	<span>
		<img src="/static/img/vi.powered.by.sven.gif" alt="Written in vim" title="Written in vim" />
		W3C 
		<a href=>HTML</a>&amp;
		<a href=>CSS</a>
		valid.
		UTF-8 encoded.
	</span><br />
	<span>© 2008 reaky All rights reserved, all wrongs observed.</span><br />
	<span>Powered by Python Bottle sqlite3 jQuery on iPad2</span>
</footer>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
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
