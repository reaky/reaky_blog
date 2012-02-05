$(document).ready(function() {
	$('#article_comment').hide('fast');
	$('#navi_about').click(function() {
		window.history.pushState(null, document.title, $(this).attr('href'));
		window.history.replaceState(null, null, $(this).attr('href'));
		$('#main_content').load($(this).attr('href'));
		return false;
	});
	$('.article_content').toggle(function() {
		key = $(this).siblings('.article_key').text();
		$('#article_comment').hide('fast');
		$('textarea').val('');
		$(this).after($('#article_comment'));
		$('#article_comment').show('slow');
		$('#comment_form').attr("action", "/addcomment/"+key);
		$('#comments_posted').load('/listcomment/'+key);
		$('input').bind('focus', function() {
			$(this).val("");
		});
	}, function() {
		$('#article_comment').hide('fast');
	});
	$(window).scroll(function() {
		var bodyTop = document.documentElement.scrollTop + document.body.scrollTop;
		//滚动到底部时出发函数
		//滚动的当前位置+窗口的高度 >= 整个body的高度
		if(bodyTop+$(window).height()-25 >= $(document.body).height()){
			//$('#main_content').load('/show/1');
			//$('#main_content > div:last-child').after('<p>ss</p>');
			num = $('#main_content').children('.article').length;
			//alert(num);
			$.get('/show/'+num, function(data) {
				$(data).find('#main_content .article').appendTo('#main_content');
			});
		}
	});
	$('#comment_form').ajaxForm(function() { 
		var str = $('#comment_form').attr("action")+"";
		str = str.replace("addcomment", "listcomment");
		$('#comments_posted').load(str);
		$('textarea').val('');
		//alert('form ok');
	});
/*	$('#navpages > p > a').click(function() {
		window.history.pushState(null, document.title, $(this).attr('href'));
		window.history.replaceState(null, null, $(this).attr('href'));
		$('#main_content').load("/?"+$(this).attr('href').split("?")[1]);
		return false;
	});*/
});
