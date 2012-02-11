$(document).ready(function() {
	$('#article_comment').hide('fast');
	$('#navi_about').click(function() {
		window.history.pushState(null, document.title, $(this).attr('href'));
		window.history.replaceState(null, null, $(this).attr('href'));
		$.get('/about', function(data) {
			$('#main_content').html($(data).find('#about'));
		});
		$(window).unbind('scroll')
		return false;
	});
	$('#comment_form > :text').bind('focus', function() {
		if ($(this).val() == 'Name' || $(this).val() == 'Email') {
			$(this).val("");
		}
	});
	$('.article_content').live('click', function() {
		var toggled = $(this).data('toggled');
		$(this).data('toggled', !toggled);
		if (!toggled) {
			key = $(this).siblings('.article_key').text();
			$('#article_comment').hide(0);
			$('textarea').val('');
			$('#comment_form').attr("action", "/addcomment/"+key);
			$('#comments_posted').load('/listcomment/'+key);
			$(this).after($('#article_comment'));
			$('#article_comment').show('slow');
			$('html, body').animate({
				scrollTop: $('#article_comment').offset().top
				},800);
		}
		else {
			$('#article_comment').hide(0);
		}
	});
	/*$('.article_content').toggle(function() {
		key = $(this).siblings('.article_key').text();
		$('#article_comment').hide('fast');
		$('textarea').val('');
		$(this).after($('#article_comment'));
		$('#article_comment').show('slow');
		$('#comment_form').attr("action", "/addcomment/"+key);
		$('#comments_posted').load('/listcomment/'+key);
	}, function() {
		$('#article_comment').hide('fast');
	});*/
	var loading = false;
	$(window).scroll(function() {
		//judge if scroll to first post
		if ($('#main_content > div:last-child > .article_key').text() == 1) {
			$(window).unbind('scroll');
			return false;
		}
		var bodyTop = document.documentElement.scrollTop + document.body.scrollTop;
		var $buffer = $('<div />');
		//滚动到底部时触发函数
		//滚动的当前位置+窗口的高度 >= 整个body的高度
		if (!loading &&(bodyTop+$(window).height() >= $(document.body).height())) {
			loading = true;
			num = $('#main_content').children('.article').length;
			//replace the content
			//$('#main_content').load('/show/1');
			//can not load dynamic content
			//$('#main_content > div:last-child').after('<p>ss</p>');
			//asynchronous call will cause reload
			//$.get('/show/'+num, function(data) {
			//	$(data).find('#main_content .article').fadein('slow').appendTo('#main_content');
			//});
			//copy from keakon.net
			$buffer.load('/show/'+num+' #main_content > .article', function(data) {
				//alert('load ok?');
				$buffer.children().appendTo('#main_content');
				loading = false;
			});
		}
	});
	/*var loading = false;
	$(window).scroll(function() {
		var bodyTop = document.documentElement.scrollTop + document.body.scrollTop;
		if (!loading &&(bodyTop+$(window).height() >= $(document.body).height())) {
			loading = true;
			//$('#main_content').load('/show/1');
			//$('#main_content > div:last-child').after('<p>ss</p>');
			num = $('#main_content').children('.article').length;
			$.get('/show/'+num, function(data) {
				$(data).find('#main_content .article').fadein('slow').appendTo('#main_content');
			});
		}
		$(document).ready(function() {
			loading = false;
		});
	});*/
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
