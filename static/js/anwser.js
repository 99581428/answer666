
function click_a(_kid)
{

    showJSON('/answer/',"kid="+_kid);

}
function showJSON(urls,param)
{
    var xhr;
    if(window.XMLHttpRequest)
    {
        xhr = new XMLHttpRequest();
    }else if(window.ActiveXObject)
    {
        xhr = new window.ActiveXObject();
    }else
    {
        alert("浏览器版本太低，请升级浏览器")
    }
    if(xhr!=null)
    {
        xhr.open("post",urls);
    　  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.send(param);
        xhr.onreadystatechange=function()
        {

            if(xhr.readyState==4&&(xhr.status==200 || xhr.status === 304 ))
            {
                alert(xhr.responseText)
                var obj = JSON.parse(xhr.responseText );
                if(obj[0].errors=="1")
                {
                    document.querySelector('#anserde').innerHTML="积分不足，请充值"

                }
                else if(obj[0].errors=="2")
                {
                    document.querySelector('#anserde').innerHTML="请登录后查看答案"
                }
                else
                {
                    document.querySelector('#ctoa').innerHTML = ''
                    document.querySelector('#anserde').innerHTML = obj[0].kanwers
                }
            }

        }

    }
}
