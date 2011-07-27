jQuery(function($) {
	//getGoogleBuzz
	(function(){
		var username = '104418721144979799988',
			num = 10,
			div = $('#buzz');
		
	   // params for Google Feed API proxy : Buzz Feed URL, Number of Entries 
	   var data = {q:'http://buzz.googleapis.com/feeds/' + username + '/public/posted', 
	            num:num,
	            output:'json',
	            v:'1.0'};
	   // call Google Feed API
	   $.ajax({
	      url:'http://ajax.googleapis.com/ajax/services/feed/load',
	      data:data,
	      dataType:'jsonp',
	      success:function(json){
	         // json from Google Feed API was returned successfully..
 
	         // error with Google Buzz feed ?
	         if(json.responseStatus!=200) {
	            div.html('<b style="color:red">'+ json.responseDetails +'</b>');
	            return; 
	         };
	         // Buzz entries array
	         var entries= json.responseData.feed.entries;
	         var length= entries.length;
	         // no entries!
	         if(length==0) return; 
 
	         // start output by appendding a hidden unordered list
	         var ul = $('<ul class="gb" style="display:none"></ul>').appendTo(div.html(''));
 
	         // loop buzz entries
	         for(var i=0; i<length; i++){
	            // parse published-date string
	            var pDate = new Date(entries[i].publishedDate);
	            // using entry snippet version
	            var snippet = entries[i].contentSnippet;
	            // convert links that start with http to hyperlinks using regular expression
	            snippet = snippet.replace(/\b(https?\:\/\/\S+)/gi,' <a href="$1">$1</a>');
	            
	            ul.append('<li>'
	               +'<span class="gb-content">'+ snippet +'</span>'
	               +'<span class="gb-meta"><a href="'+ entries[i].link +'">'+ getTime(pDate.valueOf()) +'</a></span>'
	            +'</li>');
	         };
 
	         ul.fadeIn('slow');
	      }
	   });
	})(jQuery);
});
