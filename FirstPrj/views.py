from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World</h1>')
def about(request):
    return HttpResponse('<h1>About page</h1>')

def landingpage(request):
    return HttpResponse('<h1>Landing Page</h1>')