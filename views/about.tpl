<script type="text/javascript" src="/static/jquery-1.4.2.min.js"></script> 
<div id="about">
	<div>This is a autobiography of me, a post-student in ShangHai!</div>
	<div>A typical Geek, interesting in Computer, Rubi and Kinds of Toys.</div>
</div>
<div id="side">
<h2>Contact Me</h2>
<div><img height="14" width="16" style="padding:0 2px 0 0;margin:0;border:none" src="http://www.google.com/talk/service/resources/chaticon.gif" alt=""><img height="9" width="9" style="padding:0 2px 0 0;margin:0;border:none" src="http://www.google.com/talk/service/badge/Show?tk=z01q6amlq6uliihc3mtb3rvlednq3ktkje6ajvhem6n1ls7k3bfa6a48fsput6qf4rfpjg9q0ej1silksr1qhl61t1o1oq6i6leq46gb4gg5cr08c2ga1da5v496kpe0puj0e4tqrpl8bvrlth3r45mhgcdik4i5aq0hjvuvd&amp;w=9&amp;h=9" alt=""><a href="http://www.google.com/talk/service/badge/Start?tk=z01q6amlq6uliihc3mtb3rvlednq3ktkje6ajvhem6n1ls7k3bfa6a48fsput6qf4rfpjg9q0ej1silksr1qhl61t1o1oq6i6leq46gb4gg5cr08c2ga1da5v496kpe0puj0e4tqrpl8bvrlth3r45mhgcdik4i5aq0hjvuvd" target="_blank" title="by Gtalk">Chat with Reaky yf</a></div>
<div><a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=253052813&site=qq&menu=yes"><img border="0" src="http://wpa.qq.com/pa?p=2:253052813:45" title="by QQ">Chat with Reaky yf</a></div>
<h2>碎碎念(<strong>T.QQ</strong>)</h2>
<div id="tqq">未完待续。Loading...</div><!--tqq-->
<script type="text/javascript" src="/getqq"></script>
<script type="text/javascript" src="/static/qq.js"></script>
<h2>碎碎念(<strong>Buzz</strong>)</h2>
<div id="buzz">未完待续。Loading...</div><!--Buzz-->
<script type="text/javascript" src="/static/buzz.js"></script>
<h2>Friend links</h2>
<ul>
{% for link in links %}
	<li><a href="{{ link.address }}" title="{{ link.title }}">{{ link.title }}</a></li>
{% endfor %}
</ul>
<h2>Attention</h2>
<a><strong>To memorize the past time.</strong></a>
<ul>
	<li><a href="/static/compile.html" title="tip">compile errors</a></li>
</ul>
</div><!--side-->
