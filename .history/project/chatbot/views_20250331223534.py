from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        response_message = get_bot_response(user_message)
        return JsonResponse({'response': response_message})

    return render(request, 'chatbot/chatbot.html')

def get_bot_response(message):
    # Ajoute ta logique ici pour générer une réponse, par exemple avec ChatterBot ou une API externe
    return "Désolé, je ne comprends pas encore cette question."
