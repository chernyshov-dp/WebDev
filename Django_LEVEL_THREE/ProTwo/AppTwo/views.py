from django.shortcuts import render
from AppTwo.models import User
from . import forms


def index(request):
    form = forms.SignUpForm()

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)

    if form.is_valid():
        print("VALIDATION SUCCESS!")
        print("First name: " + form.cleaned_data['first_name'])
        print("Last name: " + form.cleaned_data['last_name'])
        print("Email: " + form.cleaned_data['email'])
    return render(request, 'AppTwo/index.html', {'form': form})


def users(request):
    webpage_list = User.objects.order_by("first_name")
    my_dict = {'user_info': webpage_list}
    return render(request, 'AppTwo/users.html', context=my_dict)
