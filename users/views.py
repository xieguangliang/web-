from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import redirect
from users.models import User
from django.views import View

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username: %s, password: %s' % (username, password))
        user = User.objects.create(username=username, password=password)
        # return JsonResponse({"message": "正在注册"})
        return redirect('/login/')


class LoginView(View):
    def get(self, request):
        username = request.session.get('username')
        if username:
            return HttpResponse('%s 用户已经登陆' % username)
            # username = request.COOKIES.get('username', ' ')
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.session.get('username')
        if username:
            return HttpResponse('%s 用户已经登陆' % username)
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
    
        try:
            user = User.objects.get(username=username, password=password)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "login failed"})
        
        else:
            
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            
            if remember != 'true':
                # response.set_cookie('username', username, max_age=14*24*3600)
                request.session.set_expiry(0)
            return JsonResponse({"message": "login succeed"})
