function form_validation1()
{
    var uname=document.formvalidation.name;
    var uemail=document.formvalidation.email;
    var uphone=document.formvalidation.phone;
    var upwd=document.formvalidation.pswd;
    
    if(uname==""||uemail==""||uphone==""||upwd=="");
    {
        alert("All fields are required")
    }
     if(uname_validation(uname,3))
       {
        if(uemail_validation(uemail))
        {
        if(uphone_validation(uphone))
        {

        if(upwd_validation(upwd,6))
        {

        }

       
    }
}
       }
       return false;
    }

function uname_validation(uname)
{
    var letters="^[A-Za-z]\\w{5, 29}$";
    if(uname.value.match(letters))
    {
        return true;
    }
    else{
        alert("name should have alphabetic characters only");
        uname.focus();
        return false;
    }
}

function email_validation(email)
{
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (uemail.value.match(mailformat))
    {
        return true;
    }
    else{
        alert("you have entered an invalidform");
        uemail.focus();
        return false;
    }
}

function uphone_validation(uphone)
{
    var phonenumber= /^\d{10}$/;
    if (uphone.value.match(phonenumber))
    {
        return true;
    }
    else{
        alert("phone shoulkd be minimum 10 number");
        return false;
    }
}

function upwd_validation(upwd,mx)
{
    var paswd_len=upwd.value.length;
    if(paswd_len==0||paswd_len>=mx)
    {
        alert("password should be minimum"+mx);
        upwd.focus();
        return false;
        
    }
}





