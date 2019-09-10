
    // 获取元素  
	var username = document.getElementById('username');
	var reg = document.getElementById('reg');  
		// 设置用户名是否满足条件的标志 false 表示没有通过，true表示通过
 	   var isUsernameOk = false;
 
    // 设置表单的提交事件，根据条件是否允许提交
		reg.onsubmit = function () { 
				var str = "";  
				var cbox = document.querySelector('#cbox');
				if (!isUsernameOk) {
					// 取消表单的默认事件,终止执行 
					 str = username.value.trim(); 
					if(str.length<=0)
					{
						document.querySelector('#username_span').className = 'error'; 
						document.querySelector('#username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
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
				var cbox = document.querySelector('#cbox'); 
				if(!cbox.checked)
				{
					document.querySelector('#cbox_span').innerHTML = '请阅读并同意用户协议';
				}
				if(!(isUsernameOk&&pwdcorr&&pwdcorr2&&cbox.checked))
				{
					return false;
					
				}  
			}
    
			// 获取焦点，设置提示信息
			username.onfocus = function () { 
				// 设置提示信息span的类名和信息
				
				document.querySelector('#username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
				document.querySelector('#username_span').className = 'tipMsg';
			}
    
    			// 失去焦点，判断是否满足条件
			username.onblur = function(){
				// 去除多余的空白字符
				var uname = this.value.trim();
				// 判断是否有非法字符(除了中英文、数字、下划线以外的字符)
				var charReg = /^[a-zA-Z][a-zA-Z0-9]{6,20}$/;  			
				if(!charReg.test(uname)) {
					// 设置错误信息
					document.querySelector('#username_span').className = 'error'; 
					document.querySelector('#username_span').innerHTML = '用户名是长度为6到20之间的字母与数字组合<br>首位必须为字母,区分大小写';
					// 设置用户名标记为false
					isUsernameOk = false;
					// 终止程序
					return;
				}	
				else {
						// 设置成功信息
						document.querySelector('#username_span').className= 'success';
						document.querySelector('#username_span').innerHTML = '可以注册';
						
						// 设置成功的标志
						isUsernameOk = true;
					} 
			} 
			  

  //密码规则验证
	 var pwd = document.querySelector('#pwd');
	 var pwd_span = document.querySelector('#pwd_span'); 
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
	var pwd2 = document.querySelector('#pwd2');
	var pwd2_span = document.querySelector('#pwd2_span');
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
	
	 var cbox = document.querySelector('#cbox'); 
	 cbox.onclick = function()
	 {
				if(!cbox.checked)
				{
					document.querySelector('#cbox_span').innerHTML = '请阅读并同意用户协议';
				}else
				{
					document.querySelector('#cbox_span').innerHTML = '';
					
				}
	 }
