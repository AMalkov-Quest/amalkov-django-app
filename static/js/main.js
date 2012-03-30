$(function(){
	$('form#find').submit(function() {
		send(
			$(this).attr('action'),
			$(this).serialize() 
		);
		return false;
	});

	alert('OK');
});

function send(url, data) {
	$('body').load(url + '?' + data + '&js=true');
};

function _send(url, data) {
	$.ajax({
		type: "GET",
		url: url,
		data: data+'&js=true',
		success: function(data) {
			alert(data);
		}
	});
};
