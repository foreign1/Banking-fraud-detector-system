from distutils.command.upload import upload
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .ml_model import Y_pred_cls, Y_mod2_cls, m_accuracy, m2_accuracy, r_score, r2_score, p_score, p2_score, f_score, f2_score
from .forms import UploadDataForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        upload_data = UploadDataForm(request)
        return render(request, 'processing.html', {"redirect_attribute": "<meta http-equiv='refresh' content='seconds'; url='{% url 'outcome' %}'} >"})

        if upload_data.is_valid():
            return render(request, 'processing.html', {'processing': 'processing'})
            # return HttpResponseRedirect('/processing/') 
    else: upload_data = UploadDataForm

    return render(request, 'index.html', {'form': upload_data})


def processing(request):
    return render(request, 'index.html', context={'processing': "Processing..."})

def output(request):
    context = {
        'model_1': {
            'model_accuracy' : (0.9986482216214319, 56792),
            'recall_score': (0.9489795918367347, 72),
            'precision_score': (0.5636363636363636, 5),
            'f-score': (0.7072243346007604, 92),
        },
        'model_2': {
            'model_accuracy': (0.9992099996488887, 56790),
            'loss_value': (0.008827306184946626, 41),
            'recall_score': (0.9693877551020408, 41),
            'precision_score': (0.6934306569343066, 2),
            'f-score': (0.8085106382978723, 83),
        }
    }
    return render(request, 'output.html', context={})