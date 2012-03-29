$(function(){
	$('form#find').submit(function() {
		send(
			$(this).attr('action'),
			$(this).serialize() 
		);
		return false;
	});
});

function send(url, data) {
	$.ajax({
		type: "GET",
		url: "",
		data: data,
		success: function() {
			alert('OK');
		}
	});
};
