# from django.core.mail import send_mail
# from django.conf import settings
#
# # def send_welcome_email(email):
# #     url = 'http://localhost:8000/'
# #     message = f'Hello! This is SkateShop! Thanks for you registration on our site!\n{url}'
# #     send_mail('SkateShop Welcome!',
# #                 message,
# #                 'jaanger@gmail.com',
# #                 [email,],
# #                 fail_silently=False
# #                 )
# from django.shortcuts import redirect
#
#
# def send_welcome_email(email):
#     # url = 'http://localhost:8000/'
#     # message = f'Hello! This is SkateShop! Thanks for you registration on our site!\n{url}'
#     # send_mail('PyShop12 Welcome!',
#     #           message,
#     #           'eelonmusk@gmail.com',
#     #           [email,],
#     #           fail_silently=False
#     #           )
#     subject = 'Hello! This is SkateShop!!'
#     message = 'Thanks for you registration on our site!'
#     email_form = settings.EMAIL_HOSTS_USER
#     recipient_list = ['receiver@gmail.com',]
#     send_mail(subject, message, email_form, recipient_list)
#     return redirect('home_page_url')
