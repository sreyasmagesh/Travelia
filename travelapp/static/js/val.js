console.log("jhghg")

$(document).ready(function(){
    $("#validation").validate({
        rules:{
            username:"required",
            // email:"required",
            email:{
                required:true,
                email:true
            },
            password:{
                required:true,
                maxlength:8,
                minlength:3
            }
        },
        message:{
            username:"please enter username",
            email:"please enter username",
            password:"please enter password"

        },
        submitHandler:function(form){
            form.submit()
        }
    })
})