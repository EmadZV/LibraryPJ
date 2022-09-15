from django.shortcuts import render, get_object_or_404, redirect

from mycart.forms import CartAddBookForm
from mycontent.context_processors import search
from mycontent.forms import BookCreateForm
from mycontent.models import Book


def landing_page(request, ):
    latest_books = Book.get_latest(self=request)
    # most_viewed_books = Book.get_most_viewed()
    # most_liked_books = Book.get_most_liked()
    # most_discounted_books = Book.get_most_discounted()
    context = {
        'latest_books': latest_books,
        # 'most_viewed_books': most_viewed_books,
        # 'most_liked_books': most_liked_books,
        # 'most_discounted_books': most_discounted_books,
    }
    return render(request, 'mycontent/landing_page.html', context)


def search_result(request, ):
    import pdb;
    pdb.set_trace()

    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['title']:
                result = Book.objects.filter(title=cd['title'])
            if cd['title']:
                result = Book.objects.filter(title=cd['author'])
    else:
        result = None

    return render(request, 'mycontent/landing_page.html', {'result': result})


def book(request, book_slug):
    mybook = get_object_or_404(Book, slug=book_slug)
    comments = mybook.get_comments()
    cart_book_form = CartAddBookForm()
    context = {
        'book': mybook,
        'comments': comments,
        'cart_book_form': cart_book_form,
    }
    return render(request, 'mycontent/book.html', context)


def book_create(request):
    new_book = None
    user = request.user
    # if user is not
    if request.method == 'POST':
        form = BookCreateForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)

            new_book.user = user
            new_book.save()
        else:
            print('is not valid', form.errors)
    else:
        form = BookCreateForm(request.POST)
    return render(request, 'mycontent/book_create.html', context={'form': form,
                                                                  'newpost': new_book})
