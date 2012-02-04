<html>
<head>
<meta charset="UTF-8" />
<title>Blog editor</title>
<link type="image/x-icon" href="/static/img/favicon.ico" rel="shortcut icon"/>
<link type="text/css" rel="stylesheet" href="/static/blog.css" media="screen" />
</head>
<body>
<div id="editor" style="margin:20px">
<form action="/updatepost/{{ post[0] }}" method="post" id="editorform" onsubmit="document.charset='utf-8';" accept-charset="utf-8">
	<input type="text" name="title" value="{{ post[1] }}" style="width:60%" tabindex="1" />
	<input type="text" name="date" value="{{ post[3] }}" style="width:15%" tabindex="1" />
	<textarea name="postcontent" tabindex="2" style="width:100%" rows="20">{{ post[4] }}</textarea>
	<input name="id" type="hidden" id="id" value="{{ post[0] }}">
	<input name="submit" type="submit" id="submit" tabindex="3" value="Submit" />
</form>
</div>
</body>
</html>
