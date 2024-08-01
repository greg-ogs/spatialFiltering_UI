from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .backend_algorithms import ANN


def index(request):
    template_name = 'index.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render())


def pid_controller(request):
    template_name = 'PIDtemplate.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render())


def ann_controller(request):
    template_name = 'anntemplate.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render())


def ann_train(request):
    template_name = 'anntemplate.html'
    template = loader.get_template(template_name)
    stage1 = ANN.Stage1ANN()
    stage1.load_data()
    stage1.prepare_data()
    stage1.set_model()
    stage1.train()
    context = {'oktrain': 1}
    return HttpResponse(template.render(context))


def ann_tests(request):
    template_name = 'anntest.html'
    template = loader.get_template(template_name)
    ok_test = ["Modules tested and passed:"]
    print("Testing methods...")
    stage1 = ANN.Stage1ANN()
    print("init OK")
    ok_test.append("INIT")
    stage1.load_data()
    print("Load data test OK")
    ok_test.append(" LOAD DATA ")
    stage1.prepare_data()
    print("Prepare data test OK")
    ok_test.append("PREPARE DATA")
    stage1.set_model()
    print("Model set test OK")
    ok_test.append("MODEL SET")
    stage1.train()
    print("Model training test OK")
    ok_test.append("MODEL TRAIN")
    from tensorflow import keras
    reconstructed_model = keras.models.load_model("model.keras")
    reconstructed_model.summary()
    context = {
        'tested': ok_test
    }
    return HttpResponse(template.render(context))


def nd_controller(request):
    template_name = 'ndtemplate.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render())
