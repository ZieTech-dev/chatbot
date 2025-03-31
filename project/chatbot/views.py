from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialisation du chatbot (exécuté une seule fois au démarrage)
chatbot = ChatBot('MonChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.french')

def get_bot_response(message):
    response = chatbot.get_response(message)
    return str(response)

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        if user_message:
            response_message = get_bot_response(user_message)
            return JsonResponse({'response': response_message})
        else:
            return JsonResponse({'error': 'Message vide'}, status=400)
    return render(request, 'chatbot/chatbot.html')