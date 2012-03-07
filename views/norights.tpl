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
				<li><a href="/norights"><span>Comment_Board</span></a></li>
				<li><a href="{{ login_url }}">Login</a></li>
			</ul>
		</div>
		<div id="main_content">
			<div class="article">
			<div class="article_title"> Comment_Board </div>
			<div class="article_content">{{ article.content }}</div>
			<div class="article_comment">
				<div class="comments_posted"></div>
				<form class="comment_form" action="/addcomment" method="post">
					<div>
						<input type="text" name="auth" value="Name" />
						<input type="text" name="email" value="Email" />
						<input name="submit" type="submit" value="Submit" />
					</div>
					<div><input type="hidden" name="article_key" class="article_key" value="{{ article.key }}" /></div>
					<div><textarea name="content" rows="" cols="" value="要不留下点什么？"></textarea></div>
				</form>
			</div>
		</div>
		<div id="footer_bar">{% include "footer_bar.html" %}</div>
	</div></body>
</html>
