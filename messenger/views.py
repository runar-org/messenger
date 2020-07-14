from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Encryption, Message


def index(request):
    template = loader.get_template('index.html')
    messages = { 'messages': 'fake business' }
    return HttpResponse(template.render(messages, request))

def send(request):
    template = loader.get_template('send/index.html')
    messages = { 'messages': 'fake business' }
    return HttpResponse(template.render(messages, request))

def receive(request):
    template = loader.get_template('receive/index.html')
    messages = { 'messages': 'fake business' }
    return HttpResponse(template.render(messages, request))

def result(request):
    template = loader.get_template('result/index.html')
    messages = { 'messages': 'fake business' }
    return HttpResponse(template.render(messages, request))