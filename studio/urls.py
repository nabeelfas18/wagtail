from django.urls import path
from django.views.generic.base import TemplateView
from studio import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    # path('work/', TemplateView.as_view(template_name='work_page.html'), name = "work"),
    # path('about/',TemplateView.as_view(template_name='about_page.html'), name = "about"),
    # # path('blog/',TemplateView.as_view(template_name='blog_page.html'), name="blog"), 
     path('contact/',views.ContactView.as_view(), name="contact"),
    # path('work', views.work, name = "work"),
 ]