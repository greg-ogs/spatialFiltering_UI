from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .backend_algorithms import ANN


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
    print("Testing")
    # stage1 = ANN.Stage1ANN
    # print("Testing init")
    # stage1.load_data()
    # print("Testing load data")
    # stage1.prepare_data()
    # stage1.set_model()
    # stage1.train()
    return HttpResponse(template.render())


def nd_controller(request):
    template_name = 'ndtemplate.html'
    template = loader.get_template(template_name)
    print("Testing")
    return HttpResponse(template.render())
