from django.shortcuts import render, redirect
from studio.models import Contact
from django.conf import settings
from django.core.mail import send_mail
from django.views import View
from django.views.generic import TemplateView
from studio_project.settings.base import EMAIL_HOST_USER



class ContactView(View):
    def get(self, request):
        return render(request, "contact_page.html")

    def post(self, request):
        # reg = Contact()
        # # storing html form field values into model
        # reg.name = request.POST.get("name")
        # reg.email = request.POST.get("email")
        # reg.subject = request.POST.get("subject")
        # reg.message = request.POST.get("message")
        # nameerror = ""
        # emailerror = ""
        # subjecterror = ""
        # messageerror = ""

        # if reg.email == "":  # checking email is null or not
        #     emailerror = "Please enter your email"
        # if reg.subject == "":  # checking subject is null or not
        #     subjecterror = "Please enter your subject"
        # if reg.message == "":  # checking message is null or not
        #     messageerror = "Please enter your message"
        # if len(reg.name) < 3 or len(reg.name) > 25:  # checking name between 3 and 25
        #     nameerror = "Name shoud be between 3 and 25 character"
        # if reg.name == "":  # checking first name is null or not
        #     nameerror = "Please enter your name"

        # values = {
        #     "nameerror": nameerror,
        #     "emailerror": emailerror,
        #     "subjecterror": subjecterror,
        #     "messageerror": messageerror,
        #     "name": reg.name,
        #     "email": reg.email,
        #     "subject": reg.subject,
        #     "message": reg.message,
        # }

        # # checking backend validations
        # if (
        #     reg.name == ""
        #     or reg.email == ""
        #     or reg.subject == ""
        #     or reg.message == ""
        #     or len(reg.name) < 3
        #     or len(reg.name) > 25
        # ):
        #     # if not valid return to applicant registration form
        #     return render(request, "contact_page.html", {"values": values})
        try:
            subject = 'welcome to GFG world'
            message = 'Hi  thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['nabeelfas18@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            # reg.save()  # Inserting applicant details into the database
            return redirect("/contact")
        except:
            pass

