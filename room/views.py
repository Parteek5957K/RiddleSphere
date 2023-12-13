from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import random
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.conf import settings
from django.shortcuts import get_object_or_404
import os


# Create your views here.

def download_pdf(request):
    # Specify the relative path to your PDF file within the static folder
    pdf_relative_path = 'pdf/file.pdf'

    pdf_path = os.path.join(settings.BASE_DIR, 'static', pdf_relative_path)

    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="file.pdf"'
        return response


def get_answer(request):
    answers = ['1', '2', '3', '4', '5']
    return JsonResponse({'answers': answers})


def roomvisit(request):
    title = "Bunker Room"
    description = [
        "In the heart of a desolate mountain range, you find yourself alone and isolated. A serene retreat turns into a gripping tale of survival when a cosmic collision rocks the landscape. Without warning, you discover a hidden bunker, its metallic walls providing an unexpected refuge.",
        "As the echoes of the asteroid impact reverberate around you, a digital display blinks to life, revealing a countdown timer. Trapped within the confines of the bunker, your only means of escape lies in solving a series of cryptic puzzles that materialize on the screen, each one a key to unlocking the virtual door.",
        "The distant mountains, once a symbol of tranquility, now stand as silent witnesses to your struggle. The enigmatic symbols on the screen and the holographic sequences hint at the trajectory of the cosmic chaos outside. With each solved puzzle, the urgency of your situation intensifies, and the metallic walls seem to close in.",
        "As you delve deeper into the virtual chambers, the challenges become more intricate, testing your wit and determination. The soundtrack pulses with tension, mirroring the rhythmic beat of your quickened heartbeat. The escape from this digital confinement becomes a race against time, with the echoes of the asteroid impact serving as a constant reminder of the cosmic enigma that surrounds you."]
    context = {'desc': description, 'title': title}
    return render(request, 'parallax-1.html', context)

def roomvisit2(request):
    title = "Whispers in the Shadows"
    context = {'title': title}
    return render(request, 'parallax-2.html', context)

def roomvisit3(request):
    title = "Whispers in the Shadows"
    description = [
        "In the heart of a desolate mountain range, you find yourself alone and isolated. A serene retreat turns into a gripping tale of survival when a cosmic collision rocks the landscape. Without warning, you discover a hidden bunker, its metallic walls providing an unexpected refuge.",
        "As the echoes of the asteroid impact reverberate around you, a digital display blinks to life, revealing a countdown timer. Trapped within the confines of the bunker, your only means of escape lies in solving a series of cryptic puzzles that materialize on the screen, each one a key to unlocking the virtual door.",
        "The distant mountains, once a symbol of tranquility, now stand as silent witnesses to your struggle. The enigmatic symbols on the screen and the holographic sequences hint at the trajectory of the cosmic chaos outside. With each solved puzzle, the urgency of your situation intensifies, and the metallic walls seem to close in.",
        "As you delve deeper into the virtual chambers, the challenges become more intricate, testing your wit and determination. The soundtrack pulses with tension, mirroring the rhythmic beat of your quickened heartbeat. The escape from this digital confinement becomes a race against time, with the echoes of the asteroid impact serving as a constant reminder of the cosmic enigma that surrounds you."]
    context = {'desc': description, 'title': title}
    return render(request, 'parallax-3.html', context)

def roombunker(request):
    title = "Bunker Room"
    context = {'title': title}
    return render(request, 'bunker-room.html', context)


def roomlibrary(request):
    title = "University Library"
    context = {'title': title}
    return render(request, 'library-room.html', context)


def get_serial_message(request):
    messages = [
        "First Hint in 5mins",
        "Message 2",
        "Message 3",
        # Add more messages as needed
    ]

    current_index = request.session.get('message_index', 0)
    next_index = (current_index + 1) % len(messages)
    request.session['message_index'] = next_index

    return JsonResponse({'message': messages[current_index]})


def quizques(request):
    response = render(request, 'quiz.html')
    response['X-Frame-Options'] = 'SAMEORIGIN'

    return response


@csrf_exempt
@require_POST
def submit_game(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        puzzle_times = data.get('puzzleTimes', {})
        total_seconds = data.get('totalSeconds', 0)
        print(data, total_seconds)
        # Process and save the data in your database
        # ...

        return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
