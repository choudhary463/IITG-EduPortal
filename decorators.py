from functions import * 
from django.shortcuts import redirect


def login_required(func):
    def wrapper(*args,**kwargs):
        req = args[0]
        if(user_authenticated(req)):
            return func(*args,**kwargs)
        else:
            return redirect('accounts:login')
    return wrapper
