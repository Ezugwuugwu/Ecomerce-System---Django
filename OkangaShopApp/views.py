from django.shortcuts import render, redirect
from django import forms
from .forms import ProjectForm, UserRegisterForm
from .models import Okanga
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def okanga_page(request):
    articles = ProjectForm()
    data = request.POST

    if request.method == "POST":
        article = ProjectForm(data=data)
        if article.is_valid():
            article.save()
            article = ProjectForm()

            return redirect('get_all_articles')
    return render(request, 'okanga_page.html', {"article": articles})

def get_all_items(request):
    all_Items = Okanga.objects.all().order_by('-date_created')
    return render(request, 'article_list.html', {"item": all_Items})


def retrieve_project(request, id):
    if Okanga.objects.filter(id=id).exists():
        project = Okanga.objects.get(id=id)
    else:
        project ={}
    return render(request, "project_details.html", {"project": project})

def delete_project(request, id):
    # context = {}
    # deleted_article = get_object_or_404(Okanga, id =id)
    # if request.method == "POST":
    #     deleted_article.delete()
    #     return redirect("get_all_articles")

    if Okanga.objects.filter(id=id).exists():
        Okanga.objects.get(id=id).delete()
        return redirect("get_all_articles")


def update_project(request, id):
    project = Okanga.objects.get(id=id)
    form = ProjectForm(instance=project)
    data = request.POST
    print(data)
    if request.method == "POST":
        form = ProjectForm(instance=project, data=data)
        if form.is_valid():
            form.save()
            return redirect('project_details', id)
        else:
            print("This object will not save")
            print("This technology should not be person")
            print(form.errors)
    return render(request, "update_project.html", {"projects": project}, {"forms": form})


def project_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('get_all_articles')
    return render(request, 'login.html')


def user_register(request):
    registerForm = UserRegisterForm()
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('login_project')

    contex = {'registerForm':registerForm}
    return render(request, "register.html",contex)