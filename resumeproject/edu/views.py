from django.shortcuts import render

# Create your views here.
def skill(request):
    context = {'contact':'active'}
    return render(request,'edu/skill.html',context)
