from django.shortcuts import render

# Create your views here.

def index(request):
    # 学习笔记的主业。
    return render(request,'leaning_logs/index.html')
