from django.core.mail import EmailMessage
def mail_send_to(user):
	email = EmailMessage(
		'Welcome to Easy Share',
		'Welcome to the world of Easy Share. You may <a href= "http://127.0.0.1:8000/">click here</a> to start.',
		'noreply.easyshare@gmail.com',
		[user.user_id],
		headers={
				"MIME-Version" : "1.0",
				"Content-Type" : "text/html",
				"charset"      : "utf-8"}
	)
	email.send(fail_silently=False)
	print "Successful in sending mail"