from django.shortcuts import render
from . import models
# Create your views here.


def tag(req):
    return render(req, 'display/index.html', {'data': models.Tag.objects.values()})


def customer(req):
    return render(req, 'display/customer.html', {'data': models.Customer.objects.values()})


def webapp(req):
    return render(req, 'display/webapp.html', {'data': models.Webapp.objects.values()})


def service(req):
    return render(req, 'display/service.html', {'data': models.service.objects.values()})


def gateway(req):
    return render(req, 'display/gateway.html', {'data': models.Gateway.objects.values()})
