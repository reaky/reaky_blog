$(document).ready(function() {
	$('.article_comment').hide('fast');
	$('#navi_bar > ul > li > a').click(function() {
		window.history.pushState(null, document.title, $(this).attr('href'));
		window.history.replaceState(null, null, $(this).attr('href'));
		$('#main_content').load($(this).attr('href'));
		return false;
	});
/*	$('#navpages > p > a').click(function() {
		window.history.pushState(null, document.title, $(this).attr('href'));
		window.history.replaceState(null, null, $(this).attr('href'));
		$('#main_content').load("/?"+$(this).attr('href').split("?")[1]);
		return false;
	});*/
	$('.article_content').toggle(function() {
		$(this).next('.article_comment').show('slow');
		key = $(this).next('.article_comment').find('.article_key').val();
		$(this).parent().find('.comments_posted').load('/listcomment?id='+key);
		$('input').bind('focus', function() {
			$(this).val("");
		});
	}, function() {
		$(this).next('.article_comment').hide('fast');
	});
	$('.comment_form').ajaxForm(function() { 
		key = $(this).parent().find('.article_content').text();
		$(this).parent().find('.comments_posted').load('/listcomment?id='+key);
	});
});
