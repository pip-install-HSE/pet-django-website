from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.

def filter_view(request):
    if request.method == 'POST':
        print(request.POST)
        questions = FilterQuestion.objects.all()
        for q in questions:
            answer = request.POST.get(q.title)
            q.cur_answer = answer
            q.save()

        return HttpResponseRedirect(reverse('personal'))

    else:
        questions = FilterQuestion.objects.all()
        context = {
            'questions': questions
        }

        return render(request, 'filter.html', context)


def personal_view(request):
    if request.method == 'POST':
        print(request.POST)
        questions = PersonalQuestion.objects.all()
        for q in questions:
            answer = request.POST.get(q.title)
            q.cur_answer = answer
            q.save()

        return HttpResponseRedirect(reverse('result'))

    else:
        questions = PersonalQuestion.objects.all()
        context = {
            'questions': questions
        }

        return render(request, 'personal.html', context)


def result(request):
    animal_list = set([x.name for x in Animal.objects.all()])
    print(animal_list)

    filter_questions = FilterQuestion.objects.all()
    personal_questions = PersonalQuestion.objects.all()

    for question in filter_questions:
        if question.title == 'Размер':
            rm_list = []
            if question.cur_answer == 'Большое животное':
                rm_list = ['Улитка', 'Еж', 'Шиншилла', 'Морская Свинка', 'Хомяк']

            if question.cur_answer == 'Среднее':
                rm_list = []

            if question.cur_answer == 'Маленькое':
                rm_list = ['Хаски', 'Кошка', 'Собака', 'Черепаха', 'python']

            for x in rm_list:
                try:
                    animal_list.remove(x)
                except KeyError:
                    pass

        if question.title == 'Продолжительность жизни':
            rm_list = []
            if question.cur_answer == '1 - 3 года':
                rm_list = ['Попугай', 'python', 'Кошка', 'Еж']

            if question.cur_answer == '3 - 5 лет':
                rm_list = ['Хомяк', 'Шиншилла', 'Кролик']

            if question.cur_answer == '5 - 10 лет':
                rm_list = []

            if question.cur_answer == '10 - 20 лет':
                rm_list = ['Улитка', 'Рыбка',
                           'Морская Свинка', 'Хомяк',
                           'Шиншилла',
                           'Кролик', 'Хорек']

            if question.cur_answer == '20 и больше лет':
                rm_list = ['Улитка', 'Попугай', 'Еж',
                           'Рыбка', 'Кошка', 'Собака', 'Морская Свинка', 'Хомяк',
                           'Шиншилла',
                           'Кролик', 'Хорек', 'Хаски']

            for x in rm_list:
                try:
                    animal_list.remove(x)
                except KeyError:
                    pass

        if question.title == 'Шерсть/оперение':
            rm_list = []
            if question.cur_answer == 'Шерсть':
                rm_list = [
                    'Улитка', 'Попугай', 'Еж', 'Черепаха', 'Рыбка','python','Хамелеон', ]

            if question.cur_answer == 'Оперение':
                rm_list = ['Улитка',
                           'Еж', 'Черепаха', 'Рыбка',
                           'Кошка', 'Собака', 'Морская Свинка',
                           'Хомяк', 'python',
                           'Шиншилла', 'Хамелеон',
                           'Кролик', 'Хорек', 'Хаски']

            if question.cur_answer == 'Отсутствует и то, и то':
                rm_list = ['Попугай', 'Кошка', 'Собака', 'Морская Свинка', 'Хомяк',  'Шиншилла', 'Кролик', 'Хорек', 'Хаски']

            for x in rm_list:
                try:
                    animal_list.remove(x)
                except KeyError:
                    pass

        if question.title == 'Характер':
            rm_list = []
            if question.cur_answer == 'Спокойный':
                rm_list = ['Хаски', 'Кролик', 'Еж', 'Рыбка']

            if question.cur_answer == 'Тихий (буквально бесшумный)':
                rm_list = ['Улитка', 'Еж', 'Черепаха', 'Рыбка', 'python', 'Шиншилла', 'Хамелеон', ]

            if question.cur_answer == 'Весёлый':
                rm_list = ['Улитка', 'Попугай', 'Еж', 'Черепаха', 'Рыбка', 'python', 'Хамелеон', ]

            if question.cur_answer == 'Агрессивный':
                rm_list = ['Улитка', 'Попугай', 'Еж', 'Черепаха', 'Рыбка', 'Морская Свинка', 'Хомяк', 'Шиншилла',
                           'Кролик', 'Хорек', ]

            if question.cur_answer == 'Задиристый':
                rm_list = ['Улитка', 'Еж', 'Черепаха', 'Рыбка', 'Морская Свинка', 'Хомяк', 'Хорек', ]

            if question.cur_answer == 'Ласковый':
                rm_list = ['Попугай', 'Рыбка', 'Хамелеон']

            for x in rm_list:
                try:
                    animal_list.remove(x)
                except KeyError:
                    pass

        if question.title == 'Сложность в уходе':
            rm_list = []
            if question.cur_answer == 'Выгуливание':
                rm_list = ['Попугай', 'Рыбка', 'Морская Свинка', 'Хомяк', 'Хамелеон']

            if question.cur_answer == 'Дрессировка':
                rm_list = ['Улитка', 'Еж', 'Черепаха', 'Рыбка', 'Морская Свинка', 'Шиншилла', 'Хамелеон', 'Кролик', ]

            if question.cur_answer == 'Постоянный уход за шерстью и когтями':
                rm_list = ['Улитка', 'Попугай', 'Еж', 'Черепаха', 'Рыбка', 'python', 'Хамелеон', ]

            if question.cur_answer == 'Нет особых сложностей в уходе':
                rm_list = ['Улитка', 'Еж', 'Рыбка', 'Хомяк', 'python', ]

            for x in rm_list:
                try:
                    animal_list.remove(x)
                except KeyError:
                    pass

    points = 0

    for question in personal_questions:
        ans = PersonalQuestionUnit.objects.get(text=question.cur_answer)
        point = ans.point
        points += point

    delta = 1e9

    animal_choice = Animal.objects.get(name='Кошка')

    for animal in animal_list:
        a = Animal.objects.get(name=animal)
        if abs(a.point - points) < delta:
            delta = abs(a.point - points)
            animal_choice = a

    try:
        animal_list.remove(animal_choice.name)
    except KeyError:
        pass

    context = {
        'animal': animal_choice,
        'animal_list': animal_list,
        'points': points,
    }

    return render(request, 'result.html', context)
