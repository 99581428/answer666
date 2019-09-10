window.onload =function()
    {

        $("#").click(function(){      $.ajax({         url: './terminal_svr',         type: 'POST',         data: {},         dataType: 'json',
    timeout: 10000,         success: function(result) {         if ( result.result == "post_success" ) {           $("#ntfText").html("发起成功");         }
    else
        {
            $("#ntfText").html("重复发起了");         }         }        });   });
}s