from django.shortcuts import render

# Create your views here.

def index(request) :
    print('>>>>>> debug, client url http://127.0.0.1:8000/html/index , index() call ~~ ')

  # business logic
  # client request params
  # model(DB) - CRUD

    return render(request, 'html/index.html')

def tag(request) :
    print('>>>>>> debug, client url http://127.0.0.1:8000/html/index/basic_tag , tag() call ~~ ')

    return render(request, 'html/tag.html')
