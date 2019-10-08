window.onload = function()
{
	var btnSearch = document.getElementById('btn_search');
	btnSearch.onmousedown	= function()
	{
		btnSearch.className = 'button1'
	};
	btnSearch.onmouseup= function()
	{
		btnSearch.className = 'button';
	};
    $("#btn_search").click(function() {
    	if(chaeckKey($('#searchkey').val())) {

            window.location.href = '/search/' + "?key=" + encodeURI(encodeURI($('#searchkey').val()));
    		return false;
        }
	});
 	var chaeckKey = function (str) {

			if (str.length < 2) {
			  alert("请输入至少两位字符");
			  return false;
			}
			str = str.replace(/(^\s*)|(\s*$)/g, '');//去除空格;
			if (str == '' || str == undefined || str == null) {
			   alert("请正确输入表达式");
			  return false;
			}
			return true;
		};
}