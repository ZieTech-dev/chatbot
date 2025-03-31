from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    # Ajoutez d'autres URL ici si nécessaire
]
