

function validate_required(field,alerttxt)
{
with (field)
  {
  if (value==null||value=="")
    {alert(alerttxt);return false}
  else {return true}
  }
}
function validate_required1(field,box,alerttxt)
{
with (field)
  {
  if (field.value^box.value)
    {alert(alerttxt);return false}
  else {return true}
  }
}

function validate_form(thisform)
{
with (thisform)
  {
  if (validate_required(xia,"albums must be filled out!")==false)
    {xia.focus();return false}
  if (validate_required1(fk1,box1,"请选择照片或者改为不上传")==false)
    {fk1.focus();return false}
  }
}
