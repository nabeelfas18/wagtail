from django.shortcuts import render, redirect
from .models import Contact, EmailSnippet
from django.core.mail import send_mail
from django.views import View
from django.views.generic import FormView
from studio.forms import ContactForm
from django import forms
from studio_project.settings import emailtest
import smtplib, ssl
from email.message import EmailMessage
from studio import models
from django.contrib import messages

class ContactView(FormView):

    template_name = "contact_page.html"
    form_class = ContactForm
    success_url = '/contact/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mypublications"] = EmailSnippet.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        smtp_server = "smtp.gmail.com"
        port = 465
        sender_email = "studioproject77@gmail.com"
        password = "ufauzimjybgrzsoy"
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        server.login(sender_email, password)
        msg = EmailMessage()
        msg.set_content(form.cleaned_data["message"])
        msg["Subject"] = form.cleaned_data["subject"]
        msg["From"] = "studioproject77@gmail.com"
        msg["To"] = "nabeela@alokin.in"
        server.send_message(msg)
        messages.success(self.request,"Thank You For Your Enquiry")
        return redirect("/contact")

class IndexView(View):
    def get(self, request):
        return redirect("/work")
