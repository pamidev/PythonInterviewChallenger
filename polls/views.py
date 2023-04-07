from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import AddQuestionForm
from .models import Question


login_required(login_url='index')
def quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            answer = request.POST.get(q.question)
            items = vars(q)
            print(items[answer])
            if q.correct_answer == items[answer]:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'percent': percent,
            'total': total,
            'correct': correct,
            'wrong': wrong,
        }
        return render(request, 'polls/results.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'polls/quiz.html', context)


login_required(login_url='index')
def add_question(request):
    if request.user.is_authenticated:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'polls/add_question.html', context)
    else:
        return redirect('index')
