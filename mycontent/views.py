from django.shortcuts import render, get_object_or_404

from mycontent.models import Book


def landing_page(request):
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


def book(request, book_slug):
    mybook = get_object_or_404(Book, slug=book_slug)
    comments = mybook.get_comments()

    context = {
        'book': mybook,
        'comments': comments
    }
    return render(request, 'mycontent/book.html', context)

