from django.shortcuts import render
from django.http import JsonResponse


def get_answer(request):
    answers = [1, 2, 3, 4]

    # Return answers as JSON
    return JsonResponse({'answers': answers})


def puzzle1(request):
    return render(request, '1.html')


def puzzle2(request):
    return render(request, '2.html')


def puzzle3(request):
    return render(request, '3.html')

def puzzle4(request):
    return render(request, '4.html')

def puzzle5(request):
    return render(request, '5.html')
