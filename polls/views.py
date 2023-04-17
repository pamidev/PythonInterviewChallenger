from django.shortcuts import redirect, render
from .forms import AddQuestionForm
from .models import Question


def questions_all():
    questions = Question.objects.filter(is_verified=True)
    return questions


def questions_3():
    questions = Question.objects.filter(is_verified=True).order_by('?')[:3]
    return questions


def results(request):
    if request.user.is_authenticated:
        questions = questions_all()
    else:
        questions = questions_3()

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
        'percent': percent,
        'total': total,
        'correct': correct,
        'wrong': wrong,
    }
    return context


def quiz(request):
    if request.method == 'POST':
        context = results(request)
        return render(request, 'polls/results.html', context)
    else:
        if request.user.is_authenticated:
            questions = questions_all()
        else:
            questions = questions_3
        context = {
            'questions': questions
        }
        return render(request, 'polls/quiz.html', context)


def add_question(request):
    if request.user.is_authenticated:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('thanks')
        context = {'form': form}
        return render(request, 'polls/add_question.html', context)
    else:
        return redirect('home')
