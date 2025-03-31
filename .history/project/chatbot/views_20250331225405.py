from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        response_message = get_bot_response(user_message)
        return JsonResponse({'response': response_message})

    return render(request, 'chatbot/chatbot.html')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Création du chatbot
chatbot = ChatBot('MonChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.french')  # Charge le corpus en français

def get_bot_response(message):
    response = chatbot.get_response(message)
    return str(response)
