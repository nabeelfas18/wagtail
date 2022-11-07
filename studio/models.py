
from django.db import models

from modelcluster.fields import ParentalKey
import uuid
from wagtail.models import Page, Orderable
from ckeditor.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class WorkPage(Page):
    intro = RichTextField(blank=True)


class WorkDetailsPage(Page):
    name = models.CharField(max_length=250,null=True)
    subtitle = models.CharField(max_length=250,null=True)
    description=RichTextField(max_length=5000,null=True)
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.thumbnail.first()
        if gallery_item:
            return gallery_item.thumbnail
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('thumbnail', label="Thumbnail images"),
        
    ]
class workDetailsPagethumbnailImage(Orderable):
 
    page = ParentalKey(WorkDetailsPage, on_delete=models.CASCADE, related_name='thumbnail')

    thumbnail= models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,related_name='thumbnail',blank=True
    )
    panels = [
        FieldPanel('thumbnail'),

    ]


class workDetailsPageGalleryImage(Orderable):
 
    page = ParentalKey(WorkDetailsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image')

    ]
class AboutPage(Page):
    max_count = 1
    name = models.CharField(max_length=250,null=True)
    subtitle = models.CharField(max_length=250,null=True)
    description=RichTextField(max_length=5000,null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
class AboutPageGalleryImage(Orderable):
 
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]



class BlogPage(Page):
    intro = RichTextField(blank=True,  max_length = 100)


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogDetailsPage(Page):
    blog_title = models.CharField(blank=True,  max_length = 100)
    blog_date = models.DateField("Post date",null=True)
    blog_description = RichTextField(blank=True, max_length = 5000)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_date'),
        FieldPanel('blog_description'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageImage(Orderable):
    max_count = 1
    page = ParentalKey(BlogDetailsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]

class Contact(models.Model):  
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    email = models.EmailField(max_length=50) 
    subject=models.CharField(max_length=200)
    message= models.CharField(max_length=500)
