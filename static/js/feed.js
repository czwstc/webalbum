function change(arg,user_id){
//         if(user_id == '-1')
//         {
//             window.navigate("login.html");
//             console.log("11111")
//         }
//         else{
         var className = document.getElementById(arg).className;
         if( className == "btn btn-primary btn-sm")
         {
             document.getElementById(arg).className ="btn btn-default btn-sm";
         }
         else
         {
            document.getElementById(arg).className ="btn btn-primary btn-sm";
         }
        var name =  document.getElementById(arg).name;//从第一个输入框里获取数据
            $.ajax({
                url:"/feed",//调用的是这个url对应的那个Handler
                type:"POST",//Post方法
                data:{className:className,name:name},//要往服务器传递的数据
                success:function(data){
                    var obj = jQuery.parseJSON(data);//获取的数据一般为json格式，用这个方法来解析数据
                    console.log(obj.status);
                    console.log(obj.message);
                    console.log(obj.data);
                    $("#"+arg).html("点赞"+obj.data.length+"人");
                    if(obj.data.length >= 3)
                    {
                         $("#m"+arg).html(obj.data[0]+","+obj.data[1]+"...已赞");
                    }
                    else if(obj.data.length == 2)
                    {
                         $("#m"+arg).html(obj.data[0]+","+obj.data[1]+"已赞");
                    }
                    else if(obj.data.length == 1)
                    {
                         $("#m"+arg).html(obj.data[0]+"已赞");
                    }
                    else
                    {
                         $("#m"+arg).html("");
                    }
                },
                error:function(){//获取失败
                    console.log("failed");
                }
            });
            
 }
//评论区的js
//兼容火狐、IE8
//显示遮罩层
var c_feed_id;
var p_feed_id;
var comment_location;
function showMask(c_location, feed_id, photo_id){
    $('#mask').modal('show');
    $("#textarea").val("");
    c_feed_id = feed_id;
    p_feed_id = photo_id;
    comment_location = c_location;
    console.log(feed_id);
    console.log(c_location);
}
//隐藏遮罩层
function hideMask(flag){
   if(flag == '1')
   {
        var comment_body = $("#textarea").val();
        console.log(comment_body);
        $.ajax({
            url:"/feed",//调用的是这个url对应的那个Handler
            type:"POST",//Post方法
            data:{comment_body:comment_body,c_feed_id:c_feed_id,p_feed_id:p_feed_id},//要往服务器传递的数据
            success:function(data){
                var obj = jQuery.parseJSON(data);//获取的数据一般为json格式，用这个方法来解析数据
                console.log(obj.status);
                console.log(obj.message);
                console.log(obj.comment_bodys[0]);
                console.log(obj.user_name);
                var len = obj.comment_bodys.length;
                $("#"+ comment_location).html("评论"+len+"条");
                $("#comments"+String(c_feed_id)).append("<p>"+obj.user_name+":"+obj.comment_bodys[len-1]+"</p>");
            },
            error:function(){//获取失败
                console.log("failed");
            }
        });

   }
   $('#mask').modal('hide');
}


function feed_delete(feed_id, feed_time){
        console.log(feed_id);
        console.log(feed_time);
        $.ajax({
            url:"/feed",//调用的是这个url对应的那个Handler
            type:"POST",//Post方法
            data:{feed_id:feed_id},//要往服务器传递的数据
            success:function(data){
                var obj = jQuery.parseJSON(data);//获取的数据一般为json格式，用这个方法来解析数据
                console.log(obj.status);
                console.log(obj.message);
                var main_body = document.getElementById("main_body");
                var comp = document.getElementById(feed_time);
                main_body.removeChild(comp);
            },
            error:function(){//获取失败
                console.log("failed");
            }
        });
}


function comment_delete(){
    alert("aaaaaa")
}