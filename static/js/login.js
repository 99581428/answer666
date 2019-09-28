window.onload = function() {
             var username = document.getElementById('username');
             var pwd = document.getElementById('pwd')
	        var logi = document.getElementById('user_login');
		// 设置用户名是否满足条件的标志 false 表示没有通过，true表示通过
 	     var isUsernameOk = false;

    // 设置表单的提交事件，根据条件是否允许提交
		logi.onsubmit = function () {
		    var str1 = username.value.trim();
		    var str2 = pwd.value
		    if(str1.length<6)
            {
                return false;
            }
            if(str2.length<8)
            {
                return false;
            }
        }
}