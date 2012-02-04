<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Reaky yf</title>
<link type="image/x-icon" href="/static/img/favicon.ico" rel="shortcut icon"/>
<link type="text/css" rel="stylesheet" href="/static/blog.css" media="screen" />
</head>
<body><div id="main_page">
<div id="navi_bar"><ul>
	<li><a id="navi_about" href="/about"><span>About</span></a></li>
	<li><a id="navi_buzz" href="/buzz"><span>Buzz</span></a></li>
	<li><a id="navi_blog" href="/blog"><span>Blog</span></a></li>
</ul></div>
<div id="main_content">
<div class="post">
<span><a href="/edit">Add a new one</a></span><br />
%for article in posts:
<span>{{ article[1] }}</span>
<span><a href="/editpost/{{ article[0] }}" title="edit this article">&nbsp;&nbsp;*Edit</a></span>
<span><a href="/deletepost/{{ article[0] }}" title="dele this article">&nbsp;&nbsp;*Dele</a></span><br />
%end
</div><!--post-->

</div>
</div>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="/static/blog.js"></script>
</body>
</html>
