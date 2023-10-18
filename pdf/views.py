from django.shortcuts import render,redirect
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'index.html',{
        'books':books,
    })

def productDetail(request):
    if request.method == 'GET':
        title = request.GET['title']
        book = Book.objects.get(title=title)
        return render(request,'product_detail.html',{
            'book':book,
        })
    return render(request, 'product_detail.html')