from django.db import models

from wagtail.models import Page


class HomePage(Page):
    template="studio/work_page.html"