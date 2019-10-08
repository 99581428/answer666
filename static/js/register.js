
    // 获取元素  
	var username = document.getElementById('username');
	var reg = document.getElementById('reg');  
		// 设置用户名是否满足条件的标志 false 表示没有通过，true表示通过
 	   var isUsernameOk = false;
 
    // 设置表单的提交事件，根据条件是否允许提交
		reg.onsubmit = function () { 
				var str = "";  
				var cbox = document.getElementById('cbox');
				if (!isUsernameOk) {
					// 取消表单的默认事件,终止执行 
					 str = username.value.trim(); 
					if(str.length<=0)
					{
						document.getElementById('username_span').className = 'error';
						document.getElementById('username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
					}
				}
				if (!pwdcorr) {
					// 取消表单的默认事件,终止执行
					str = pwd.value;
					if(str.length<=0)
					{
						pwd_span.innerHTML ='密码长度不能低于8位';
						pwd_span.className = "strengthLv1";	
					}
				}
				if (!pwdcorr2) {
					// 取消表单的默认事件,终止执行
					str = pwd2.value;
					if(str.length<=0)
					{
						pwd2_span.innerHTML = '密码确认错误，请重新输入';
						pwd2_span.className = 'error';
					} 
				}
				var cbox = document.getElementById('cbox');
				if(!cbox.checked)
				{
					document.getElementById('cbox_span').innerHTML = '请阅读并同意用户协议';
				}
				if(!(isUsernameOk&&pwdcorr&&pwdcorr2&&cbox.checked))
				{
					return false;
					
				}  
			}
			var checkusername_1 = false
			// 获取焦点，设置提示信息
			username.onfocus = function () { 
				// 设置提示信息span的类名和信息
				document.getElementById('username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
				document.getElementById('username_span').className = 'tipMsg';
				checkusername_1 = false
			 	}
    
    			// 失去焦点，判断是否满足条件
			username.onblur = function(){
				// 去除多余的空白字符
				if (checkusername_1)
				{
					return;
				}
				checkusername_1 = true
				var uname = username.value.trim();
				// 判断是否有非法字符(除了中英文、数字、下划线以外的字符)
				var charReg = /^[a-zA-Z][a-zA-Z0-9]{6,20}$/;  			
				if(!charReg.test(uname)) {
					// 设置错误信息
					document.getElementById('username_span').className = 'error';
					document.getElementById('username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
					// 设置用户名标记为false
					isUsernameOk = false;
					alert(uname + "@1")
					// 终止程序
					return;
				}	
				else
				{
					alert(uname + "@2")
					 var xhr;
					if(window.XMLHttpRequest)
					{
						xhr = new XMLHttpRequest();
					}else if(window.ActiveXObject)
					{
						xhr = new window.ActiveXObject('Microsoft.XMLHTTP');
					}else
					{
						alert("浏览器版本太低，请升级浏览器")
					}
					var urlss= '/ajaxrg/';
					var param = 'username='+uname;
					xhr.open("post",urlss);
				　  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
					alert(uname + "@3")
					xhr.onreadystatechange=function () {
						if(xhr.readyState===4 && (xhr.status===200||xhr.status===304)){
							alert(uname + "@4" + xhr.readyState)
							var s=xhr.responseText
							if (s=="1"){
								document.getElementById('username_span').className = 'error';
								document.getElementById('username_span').innerHTML = '用户名已经注册';
								// 设置用户名标记为false
								isUsernameOk = false;
							}else
							{
								// 设置成功信息
								document.getElementById('username_span').className= 'success';
								document.getElementById('username_span').innerHTML = '可以注册';
								// 设置成功的标志
								isUsernameOk = true;

							}
						}
					}
					xhr.send(param);
				}
			}
			  

  //密码规则验证
	 var pwd = document.getElementById('pwd');
	 var pwd_span = document.getElementById('pwd_span');
	 var arr = ["", "弱", "中", "强"];
	 var pwdcorr = false;
	 pwd.onkeyup = function() {
		var level = 0;
		if (/[1-9]/.test(this.value)) {level++; }
		if (/[a-z]/.test(this.value)) { level++; }
		if (/[^a-z1-9]/.test(this.value)) {  level++ }
		if (this.value.length < 8) { 
		  pwd_span.innerHTML ='密码长度不能低于8位';
		  pwd_span.className = "strengthLv1";
		  pwdcorr = false;

		}else{
			pwd_span.innerHTML ='密码强度：' + arr[level];
			pwd_span.className = "strengthLv" + level;
			pwdcorr = true
		}
	}
	//校验密码确认
	var pwd2 = document.getElementById('pwd2');
	var pwd2_span = document.getElementById('pwd2_span');
	 var pwdcorr2 = false;
	pwd2.onkeyup = function(){
		if(pwd2.value===pwd.value&&pwdcorr)
		{
			pwd2_span.innerHTML = '密码确认成功';
			pwd2_span.className = 'success';
			pwdcorr2 = true;
		}else
		{
			pwd2_span.innerHTML = '密码确认错误，请重新输入';
			pwd2_span.className = 'error';
			pwdcorr2 = false;
		}
		
	}
	//电话号码校验
	
	 var cbox = document.getElementById('cbox');
	 cbox.onclick = function()
	 {
				if(!cbox.checked)
				{
					document.getElementById('cbox_span').innerHTML = '请阅读并同意用户协议';
				}else
				{
					document.getElementById('cbox_span').innerHTML = '';
					
				}
	 }
