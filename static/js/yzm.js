window.onload = function()
{
	$('#codebtn').click(btnCheck);
	 function btnCheck() {   
		if(checkphone()){
			if($('#yzmposition').val()==1)
			{
				window.location.href='/myinformation/' + "?phone=" + ($('#phone').val());
			}else
			{
				window.location.href='/reg/' + "?phone=" + ($('#phone').val());
			}

			return;
		} 
			$(this).addClass("on");   
			var time = 60;  				 
			$(this).attr("disabled", true);   
			var timer = setInterval(function() {    
				if (time == 0) {     
					clearInterval(timer);    
					$('#codebtn').attr("disabled", false);
					$('#codebtn').val("获取验证码");
					$('#codebtn').removeClass("on");
				} 
				else{    
					$('#codebtn').val(time + "秒后重新获取");
					time--;   
				}  
			}, 1000); 
		 } 
		 var checkphone = function()
		{
			var phones = $('#phone').val();
			alert(phones)
			if(!(/^1[3,4,5,7,8]\d{9}$/.test(phones))){
				$('#phone_span').attr("class","error")			
				$('#phone_span').html("手机号码有误，请确认");    
					return false;
			}
			$('#phone_span').attr("class","inputTextspan")			
				$('#phone_span').html("手机号用于找回密码，建议绑定");   
			return true;
		}
}

