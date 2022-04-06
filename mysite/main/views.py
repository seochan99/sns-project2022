from django.shortcuts import render

# Create your views here.
def shwomain(request):
    return render(request,'main/mainpage.html')
