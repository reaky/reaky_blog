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
		<li><a id="navi_GooglePlus" href=""><span>+Reaky</span></a></li>
		<li><a id="navi_blog" href="/"><span>Blog</span></a></li>
	</ul>
</div>
<div id="main_content">
%for article in posts:
<div class="article">
	<div class="article_title">{{ article[1] }}</div>
	<div class="article_time">{{ article[3][2:-9] }}</div>
	<div class="article_content">{{ article[4] }}</div>
</div>
%end
<div class="article_comment">
<div class="comments_posted"></div>
<form class="comment_form" action="/addcomment" method="post">
<div>
	<input type="text" name="auth" value="Name" />
	<input type="text" name="email" value="Email" />
	<input name="submit" type="submit" value="Submit" />
</div>
<div><input type="hidden" name="article_key" class="article_key" value="{{ article[0] }}" /></div>
<div><textarea name="content" rows="" cols="" value="要不留下点什么？"></textarea></div>
</form>
</div><!--end comments_posted-->
</div><!--end comment_form-->
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
</div>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="/static/jquery.form.js"></script>
<script type="text/javascript" src="/static/blog.js"></script>
</body>
</html>
