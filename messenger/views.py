from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from messenger.services import encrypt_message, decrypt_message, lookup_default_key


def error(request, exception):
    return render(request, 'error.html')


def error500(request):
    return render(request, 'error.html')


def index(request):
    return render(request, 'index.html')


def send(request):
    return render(request, 'send/index.html')


def encrypted(request):
    message = request.POST['message']
    key = request.POST['key_phrase']
    m = encrypt_message(message, key)
    generated_url = {'code': m.identifier.hex()}
    return render(request, 'encrypted.html', generated_url)


def receive(request, encryption_id):
    default_key = lookup_default_key(encryption_id)
    encryption_message = {'e_id': encryption_id, 'default_key': default_key}
    return render(request, 'receive/index.html', encryption_message)


def result(request):
    encryption_id = request.POST['e_id']
    up_key = request.POST['key']
    m = decrypt_message(encryption_id, up_key)
    data_sent = {'key': m}
    return render(request, 'result/index.html', data_sent)
