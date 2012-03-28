$(function(){
	$('#frame').attr('src', '/proxy');	
	$('#frame').load(function() {
		window._$ = window.frames[0].window.jQuery;
		_$('select#metro option').each(function(i, el){
			console.log(_$(el).text());
			$('select#metro').append(el)
		});
	});
});

function test() {
	$.ajax({               
		'url': "http://www.bn.ru/zap_fl_w.phtml?err=0", 
		'dataType': 'jsonp',            
		'complete': function(){         
			alert('OK');
		}
    });
}

function _test() {
	$.ajax({               
		'url': "http://www.bn.ru/zap_fl_w.phtml?err=0", 
		'dataType': 'jsonp',            
		'success': function(data, status, jqXHR){         
			alert('OK');
		}
    });
};
