
function validate_required(field,alerttxt)
{
with (field)
  {
  if (value==null||value=="")
    {alert(alerttxt);return false}
  else {return true}
  }
}
function validate_required1(field,b,alerttxt)
{
with (field,b)
  {
  if ((b==false))
    {
      return true}
  else {
  if( field.value==""){
    alert(alerttxt);
    return false}}
  }
}

function validate_form(thisform)
{var a = document.getElementsByName("box1");
var b = document.getElementsByName("box2");
var c = document.getElementsByName("box3");
var d = document.getElementsByName("box4");
with (thisform)
  {
  if (validate_required(xia,"请选择相册!")==false)
    {xia.focus();return false}
  if (validate_required1(fk0,a[1].checked,"请选择照片或者改为不上传")==false)
    {fk0.focus();return false}
  if (validate_required1(fk1,b[1].checked,"请选择照片或者改为不上传")==false)
    {fk1.focus();return false}
  if (validate_required1(fk2,c[1].checked,"请选择照片或者改为不上传")==false)
    {fk2.focus();return false}
  if (validate_required1(fk3,d[1].checked,"请选择照片或者改为不上传")==false)
    {fk3.focus();return false}
    
  }

}
