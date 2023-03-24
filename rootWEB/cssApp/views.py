from django.shortcuts import render
# Create your views here.

def index(request) :
    print(">>>>>> debug, path : main/ , render : css/index.html")
    return render(request , 'css/index.html')

def external(request) :
    print(">>>>>> debug, path : external/ , render : css/external.html")
    return render(request , 'css/external.html')

def selector(request) :
    print(">>>>>> debug, path : selector/ , render : css/selector.html")
    return render(request , 'css/selector.html')

def descendant(request) :
    print(">>>>>> debug, path : descendant/ , render : css/descendant.html")
    return render(request , 'css/descendant.html')

def box(request) :
    print(">>>>>> debug, path : box/ , render : css/box.html")
    return render(request , 'css/box.html')

def layout(request) :
    print(">>>>>> debug, path : layout/ , render : css/layout.html")
    return render(request , 'css/layout.html')