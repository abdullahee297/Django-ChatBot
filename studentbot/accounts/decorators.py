from django.shortcuts import redirect

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if 'username' not in request.session:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper