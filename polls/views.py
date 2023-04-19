from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import AddQuestionForm
from .models import Question
from accounts.models import User


def questions_all():
    questions = Question.objects.filter(is_verified=True)
    return questions


def questions_3():
    questions = Question.objects.filter(pk__gte=11, pk__lte=13)
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

        if q.correct_answer == items[answer]:
            score += 10
            correct += 1
        else:
            wrong += 1

    percent = round((score / (total * 10) * 100), 2)
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
            questions = questions_3()
        context = {
            'questions': questions
        }
        return render(request, 'polls/quiz.html', context)


@login_required
def add_question(request):
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            user = User.objects.get(pk=request.user.pk)
            question.who_add = user
            question.save()
            return redirect('thanks', pk=question.pk)
    else:
        form = AddQuestionForm()
    context = {'form': form}
    return render(request, 'polls/add_question.html', context)


def userAddedQuestions(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    questions = Question.objects.filter(who_add=user)
    context = {'username': user, 'questions': questions}

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        action = request.POST.get('action')
        question = get_object_or_404(Question, pk=question_id)

        if action == 'delete':
            question.delete()
            context['message'] = 'Question deleted successfully.'
        elif action == 'edit':
            question.question = request.POST.get('question')
            question.answer_1 = request.POST.get('answer_1')
            question.answer_2 = request.POST.get('answer_2')
            question.answer_3 = request.POST.get('answer_3')
            question.answer_4 = request.POST.get('answer_4')
            question.correct_answer = request.POST.get('correct_answer')
            question.save()
            context['message'] = 'Question updated successfully.'

    return render(request, 'profile', context)
