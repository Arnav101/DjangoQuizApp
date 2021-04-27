from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail, EasyQuestion, HardQuestion
import random

# Create your views here.
def index(request):
    return render(request, 'quizapp/index.html', {'error': ''})

def logoff(request):
    det = Detail.objects.get(username=request.session['username'])
    det.score = request.session['score']
    det.flag = True
    det.save()
    del request.session['username']

    return render(request, 'quizapp/index.html', {})

def question(request):
    login = 0
    if request.method == 'GET' and not request.session.get('username'):
        return render(request, 'quizapp/index.html', {'error': "Please Log in"})
    disabled = ''
    if request.POST.get('login'):
        login = 1
        timeleft = '5:00'
        request.session['timeleft'] = timeleft
        request.session['username'] = request.POST.get('username')
        det = Detail.objects.get(username=request.session['username'])
        if det.flag:
            del request.session['username']
            return render(request, 'quizapp/index.html', {'error': "You have already taken the quiz"})
        request.session['type'] = 0
        request.session['cnt'] = 0
        request.session['hcnt'] = 0
        request.session['score'] = det.score
        skip = 3
        request.session['skip'] = skip


    if request.POST.get('next'):
        
        request.session['timeleft'] = request.POST['timeleft']
        if request.session['skip'] == 0:
            disabled = 'disabled'
        skip = request.session['skip']
        if request.session['type'] == 0:
            if str(request.session['ans']) == str(request.POST['answer']):
                request.session['score'] += 3
                request.session['cnt'] += 1
                if request.session['cnt'] == 3:
                    request.session['type'] = 1
            else:
                request.session['score'] -= 1
                request.session['cnt'] = 0
        
        elif request.session['type'] == 1:
            if str(request.session['ans']) == str(request.POST['answer']):
                request.session['score'] += 6
                request.session['hcnt'] += 1
                if request.session['hcnt'] == 2:
                    request.session['skip'] += 1
                    disabled = ''
                    skip = request.session['skip']
                    request.session['hcnt'] = 0
            else:
                request.session['score'] -= 2
                request.session['cnt'] = 0
                request.session['hcnt'] = 0
                request.session['type'] = 0
        


    if request.POST.get('skip'):
        skip = request.session['skip'] - 1
        request.session['skip'] = skip
        request.session['type'] = 0
        request.session['cnt'] = 0
        request.session['hcnt'] = 0
        if request.session['skip'] == 0:
            disabled = 'disabled'


    if request.POST.get('end'):
        if request.POST.get('answer'):
            if request.session['type'] == 0:
                if str(request.session['ans']) == str(request.POST['answer']):
                    request.session['score'] += 3
                else:
                    request.session['score'] -= 1
            
            elif request.session['type'] == 1:
                if str(request.session['ans']) == str(request.POST['answer']):
                    request.session['score'] += 6
                else:
                    request.session['score'] -= 2

        det = Detail.objects.get(username=request.session['username'])
        det.score = request.session['score']
        det.flag = True
        det.save()
        del request.session['username']
        return render(request, 'quizapp/index.html', {})
        
    qsize = len(EasyQuestion.objects.all())
    if request.session['type'] == 0:
        qsize = len(EasyQuestion.objects.all())
        ques = EasyQuestion.objects.get(qno=random.randint(1, qsize))
    elif request.session['type'] == 1:
        qsize = len(HardQuestion.objects.all())
        ques = HardQuestion.objects.get(qno=random.randint(1, qsize))
    request.session['ans'] = ques.answer
    score = request.session['score']
    det = Detail.objects.get(username=request.session['username'])
    det.score = request.session['score']
    det.save()
    timeleft = request.session['timeleft']
    context = {
        'skip' : skip,
        'score' : score,
        'ques' : ques,
        'disabled' : disabled,
        'login' : login,
        'timeleft' : timeleft,
    }
    return render(request, 'quizapp/question.html', context)