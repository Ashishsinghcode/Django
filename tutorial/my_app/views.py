from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About page")

def service(request):
    return HttpResponse("Service page")
