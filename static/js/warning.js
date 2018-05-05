

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
  if ((b.value==0))
    {
      alert(alerttxt);return false}
  else {
    
    return true}
  }
}

function validate_form(thisform)
{
with (thisform)
  {
  if (validate_required(xia,"请选择相册!")==false)
    {xia.focus();return false}
  if (validate_required1(fk0,box1,"请选择照片或者改为不上传")==false)
    {fk0.focus();return false}
    
  }
}
