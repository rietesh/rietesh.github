 $("#sub_btn").click(function(){
     var email = $('#email').val();
     var name = $('#name').val()
     var message = $('#message').val()

     var data = {
        service_id: 'gmail',
        template_id: 'template_x6VY23lP',
        user_id: 'user_E3y32OLQbsP1eujYoDklv',
        template_params: {
            'from_name': name,
            'email_add':email,
            'message_html':message
            // 'g-recaptcha-response': '03AHJ_ASjnLA214KSNKFJAK12sfKASfehbmfd...'
    }
    };
     $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json'
    }).done(function(){
        $('#email').val("")
        $('#name').val("")
        $('#message').val("")
        alert("Email Sent")
    })
 })
