from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse 
from .models import Book
from .form import Bookform

# Create your views here.

def all_book(request):
    books = Book.objects.all()
    return render(request,'books.html',{'books':books})

def show_details(request,slug):
    books = get_object_or_404(Book,slug=slug)
    return render(request,'book_details.html',{'books':books})

def add_book(request):
    bookform = Bookform()
    context = {}
    try: 
        if request.method == "post":
            bookform = Bookform(request.POST,request.FILES)
            if bookform.is_valid():
                bookform.save()
                return redirect('all_book')
        else:
            bookform = Bookform()
        context = {
            'Bookform': bookform,
            'title': 'add_book'
        }
    except Exception as e:
        print(f'error in add_book => {e}')
    return render(request, 'add_book.html', context)

def edit_book(request,slug):
    editbook = get_object_or_404(Book,slug=slug)
    context = {}
    bookform = Bookform()
    try:
        if request.method == 'POST':
            bookform = Bookform(request.POST or None,request.FILES or None, instance=editbook)
            if bookform.is_valid():
                bookform.save()
                return redirect('all_book')
        
        else : 
            bookform = Bookform(instance=editbook)
        context = {
            "Bookform": bookform,
            "title": 'Edit Book'
        }

    except Exception as e:
        print(f'error in edit_book => {e}')
    return render(request, 'add_book.html', context)
    

def delete_book(request,slug):
    book = get_object_or_404(Book,slug=slug)
    book.delete()
    return redirect('books')
