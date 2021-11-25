from django.shortcuts import render
from django_two_app.models import User

# Create your views here.
def index(request):
    return render(request,'django_two_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict ={'users':user_list}
    return render(request,'django_two_app/users.html',context=user_dict)
