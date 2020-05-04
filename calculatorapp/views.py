from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from calculatorapp.logic.logic import SymPyGamma

def index(request):
    return render(request,'index.html')



def input(request):
    if request.method == "GET":
        q = request.GET['query']

        # g = SymPyGamma()
        # r = g.eval(q)
        r = eval(q)
        if not r:
            r = [{
                    "title": "Input",
                    "input": input,
                    "output": "Can't handle the input."
            }]

        mydictionary = {
            "q": q,
            "ans": r,
            "error": False,
            "result": True
        }

        return render(request, 'index.html', context=mydictionary)