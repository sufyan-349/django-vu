from django.db import models
# Create your models here.
from django.utils.html import format_html

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100,null=True)
    pdf = models.FileField(upload_to='book_pdfs')
    description = models.TextField()
    img = models.ImageField(upload_to='book_images')
    upload_date = models.DateTimeField(auto_now_add=True)

    def showing_img(self):
        return format_html(f"<img src='/media/{self.img}' style='width:50px;height:50px;border-radius:50%;'/>")


    def __str__(self) -> str:
        return self.title