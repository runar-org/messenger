from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Encryption, Message

def index(request):
    return render(request, 'index.html')

def send(request):
    return render(request, 'send/index.html')

def encrypted(request):
    message_with_key = {'message': request.POST['message'], 'key_phrase': request.POST['key_phrase']}
    return render(request, 'encrypted.html', message_with_key)

def receive(request, encryption_id=''):
    # actually store server side without passing to the view
    # encrypted_message = get_object_or_404(Encryption, key=encryption_id)
    encryption_message = {'encryption': encryption_id}
    return render(request, 'receive/index.html', encryption_message)

def result(request):
    data_sent = {'key': request.POST['key']}
    return render(request, 'result/index.html', data_sent)