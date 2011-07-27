div = $('#tqq');
var ul = $('<ul class="gb" style="display:none"></ul>').appendTo(div.html(''));
for(i=0;i<10;i++){
	ul.append('<li>'
		+'<span class="gb-content">'+qq.data[i].content+'</span>'
		+'<span class="gb-meta"><a href="http://t.qq.com/p/t/'+qq.data[i].id+'" target="_blank">'+getTime(qq.data[i].timestamp*1000)+'</a></span>'
		+'</li>');
	if(qq.data[i].type!=1){
		ul.append('<ul><li>'+qq.data[i].source.content+'<a href="http://t.qq.com/p/t/'+qq.data[i].source.id+'" target="_blank">'+getTime(qq.data[i].source.timestamp)+'</a></li></ul>');
	}
}
ul.fadeIn('slow');

function getTime(t){
	var nowDate = new Date(t);
        var _format = function(n) { return n = n < 10 ? '0' + n : n; }
        var _lformat = function(n) { return n = (n > 60 && n < 1900) ? n + 1900 : n; }
	var diff = parseInt(nowDate.getTime()/1000) - parseInt(t);
	if(diff < 60*24*30*12){
		return (nowDate.getMonth() + 1)+'月'+_format(nowDate.getDate())+'日' + ' ' +_format(nowDate.getHours())+':'+_format(nowDate.getMinutes());
	}else{
		return _lformat(nowDate.getYear())+'年'+(nowDate.getMonth() + 1)+'月'+_format(nowDate.getDate())+'日' + ' ' +_format(nowDate.getHours())+':'+_format(nowDate.getMinutes());
	}
}
