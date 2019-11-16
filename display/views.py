from django.shortcuts import render, get_list_or_404
from . import models
# Create your views here.


def tag(req):
    return render(req, 'display/index.html', {'data': get_list_or_404(models.Tag)})


def customer(req):
    return render(req, 'display/customer.html', {'data': get_list_or_404(models.Customer)})


def webapp(req):
    return render(req, 'display/webapp.html', {'data': get_list_or_404(models.Webapp)})


def service(req):
    return render(req, 'display/service.html', {'data': get_list_or_404(models.service)})


def gateway(req):
    return render(req, 'display/gateway.html', {'data': get_list_or_404(models.Gateway)})
