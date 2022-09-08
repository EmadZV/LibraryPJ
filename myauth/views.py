from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import get_user_model
from myauth.forms import MyUserCreationForm

User = get_user_model()


def sign_up(request):
    print(request.user_last_seen)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')

    else:
        form = MyUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'myauth/sign_up.html', context)
