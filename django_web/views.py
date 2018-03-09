from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "django_web/test.html")
    # return render(request, "indexA.html")

def saveSuccess(request):
    return render(request,"django_web/success.html")

def saveStudent(request):
    from django_web import  models
    if request.method == 'POST':
        #增加数据
        name = request.POST['name']
        age = request.POST['age']
        height = request.POST['height']
        weight = request.POST['weight']
        models.students.objects.create(name=name,age=age,height=height,weight=weight)

        resultVal = {'message': '添加成功',"code":0}
        return JsonResponse(resultVal)
