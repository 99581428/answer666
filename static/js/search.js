
window.onload = function()
{
	var btnSearch = document.querySelector('#btn_search');
	btnSearch.onmousedown	= function()
	{
		btnSearch.className = 'button1'
	}
	btnSearch.onmouseup= function()
	{
		btnSearch.className = 'button'
	}
		$("#btn_search").click(function() {
		var keyword = encodeURI($('#searchkey').val())
		$.get('/search/',{key:keyword},function (response, status, xhr) {

		 });
	});

}
