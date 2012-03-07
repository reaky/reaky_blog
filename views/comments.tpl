<hr />
%for comment in comments:
<div class="comment_body">
	<div class="comment_auth"><a href="mailto:{{ comment[3] }}"><b>{{ comment[2] }}</b></a></div>
	<div class="comment_content">{{ comment[4] }}</div>
	<div class="comment_date">{{ comment[5] }}</div>
</div>
%end