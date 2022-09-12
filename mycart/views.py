from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from mycontent.models import Book
from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd['quantity'], override_quantity=cd['override'])

    # import pdb;pdb.set_trace()
    return redirect('mycart:cart_detail')


def cart_remove(request, book):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book.id)
    cart.remove(book)
    return redirect('mycart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'mycart/detail.html', {'cart': cart})
