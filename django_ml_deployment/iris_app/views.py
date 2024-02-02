from django.shortcuts import render
from joblib import load


model = load('.\saved_models\models.joblib')

# Create your views here.
def predictor(request):
    return render(request, "main.html")


def form_info(request):
    sepal_len = request.GET['sepal_len']
    sepal_width = request.GET['sepal_width']
    petal_len = request.GET['petal_len']
    petal_width = request.GET['petal_width']

    y_pred = model.predict([[sepal_len, sepal_width, petal_len, petal_width]])
    if y_pred[0] == 0:
        y_pred = 'Setosa'
    elif y_pred[0] == 1:
        y_pred = 'Verscicolor'
    else:
        y_pred = 'Virginica'

    context = {'res': y_pred}
    return render(request, "result.html", context=context)
