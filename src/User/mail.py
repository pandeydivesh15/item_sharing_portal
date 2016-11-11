from django.core.mail import EmailMessage
def mail_send_to(user):
	email = EmailMessage(
		'Welcome to Easy Share',
		'''Welcome to the world of Easy Share. You may <a href= "http://127.0.0.1:8000/">click here</a> to start.<br>
                You provided following details.<br>Name:- %s<br>Userid:- %s<br>Password:- %s'''%(user.name,user.user_id,user.user_pwd),   
		'noreply.easyshare@gmail.com',
		[user.user_id],
	)
	email.content_subtype = "html"
	email.send(fail_silently=False)
	print "Successful in sending mail"
