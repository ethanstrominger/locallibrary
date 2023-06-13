from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    
    print("debug login view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', ''))
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from allauth.account.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        print('debug get success url')
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', ''))
        if redirect_to:
            self.redirect_field_value = redirect_to
        return super().get_success_url()