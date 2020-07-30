from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Encryption, Message
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def index(request):
    return render(request, 'index.html')

def send(request):
    return render(request, 'send/index.html')

def encrypted(request):
    iv = get_random_bytes(16)
    message = request.POST['message']
    key = request.POST['key_phrase']
    key = key.encode()
    key = key + (AES.block_size - (len(key) % AES.block_size)) * b'\x00'
    key = key[:32]
    message = message.encode()
    message = message + (AES.block_size - (len(message) % AES.block_size)) * b'\x00'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    coded = cipher.encrypt(message)
    message_with_key = {'message': coded.hex(), 'key_phrase': key.hex()}
    return render(request, 'encrypted.html', message_with_key)

def receive(request, encryption_id='mASuc23'):
    e = Encryption.objects.get(identifier=encryption_id)
    encryption_message = {'encryption': encryption_id, 'e': e}
    return render(request, 'receive/index.html', encryption_message)

def result(request):
    data_sent = {'key': request.POST['key']}
    return render(request, 'result/index.html', data_sent)