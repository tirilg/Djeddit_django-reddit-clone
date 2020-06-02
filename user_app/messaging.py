from django.core.mail import send_mail

## Email template for user request new password
def password_req_email(message_dict):
   alt_body = f"To reset your password, click the following link: {message_dict['reset_url']}"
            
   body = ("<html>"
               "<head></head>"
                     "<body>"
                        f"<h4>To reset your password, click <a href='{message_dict['reset_url']}'>this link</a></h4>"
                     "</body>"
            "</html>"
   )

   send_mail(
      'Password reset', 
      alt_body, 
      'kea.test.tiril@gmail.com', 
      ['kea.test.tiril@gmail.com'], 
      html_message=body,
      fail_silently=False
   )