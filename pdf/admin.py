from django.contrib import admin
from .models import Book



# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('showing_img','title','author','pdf','description','upload_date',)
    search_fields = ('title',)


    


admin.site.register(Book,BookAdmin)