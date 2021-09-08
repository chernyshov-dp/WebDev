from django.shortcuts import render
from AppTwo.models import User
# Create your views here.


def index(request):
    return render(request, 'AppTwo/index.html')


def users(request):
    webpage_list = User.objects.order_by("first_name")
    my_dict = {'user_info': webpage_list}
    return render(request, 'AppTwo/users.html', context=my_dict)
