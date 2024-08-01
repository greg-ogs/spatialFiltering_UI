from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .backend_algorithms import ANN


def algorithm_selection(request):
    template_name = 'algorithmsSelection.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render())


def pid_controller(request):
    template_name = 'PIDtemplate.html'
    template = loader.get_template(template_name)
    print("Testing")
    return HttpResponse(template.render())


def ann_controller(request):
    template_name = 'anntemplate.html'
    template = loader.get_template(template_name)
    print("Testing methods...")
    stage1 = ANN.Stage1ANN()
    print("init OK")
    stage1.load_data()
    print("Load data test OK")
    stage1.prepare_data()
    print("Prepare data test OK")
    stage1.set_model()
    print("Model set test OK")
    stage1.train()
    print("Model training test OK")
    return HttpResponse(template.render())


def nd_controller(request):
    template_name = 'ndtemplate.html'
    template = loader.get_template(template_name)
    print("Testing")
    return HttpResponse(template.render())
