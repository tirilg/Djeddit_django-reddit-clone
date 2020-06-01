from django.core.mail import send_mail

## Email template for user request new password
def new_password_req_email(message_dict):
   contents = f"""
    Forgot your password?
   No worries! Below is the token you'll need to reset your password.
   Token: {message_dict['token']}
   """
   send_mail(
      'Djeddit - forgot password',
      contents,
      'kea.test.tiril@gmail.com',
      [message_dict['email']],
      fail_silently=False
    )