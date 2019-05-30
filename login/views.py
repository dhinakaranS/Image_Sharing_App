from django.shortcuts import render

# Create your views here.
def viewHome(request):
    return render(request, 'login.html')


