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

def form(request) :
    print('>>>>>> debug, client url http://127.0.0.1:8000/html/index/form_tag , form() call ~~ ')
    return render(request, 'html/form.html')

def login(request) :
    print('>>>>>> debug, client url http://127.0.0.1:8000/html/index/login , login() call ~~ ')
    # 1. 사용자의 아이디, 패스워드를 얻어와야한다.
    # 2. model - select
    # 3. 사용자 인증에 따른 화면분기(ok, fail)
    id = request.GET['user_id']
    pwd = request.GET['user_pwd']
    print('>>>>>> debug , params : ', id, pwd)
    if id == 'jslim' and pwd == 'jslim':
        context = { 'nickName' : '나가사키'}
        return render(request, 'html/ok.html' , context)
    else :
        context = {'id': id}
        return render(request, 'html/fail.html' , context)
