from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
import django_extensions

def index_page(request):
    form = SnippetForm()
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets_list")
        return render(request, 'add_snippet.html', {'form': form})


def snippets_view(request):
    c = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов', 'snip': c}
    return render(request, 'pages/view_snippets.html', context)


def snippet(request, idx):
    c = Snippet.objects.get(pk=idx)
    context = {'pagename': 'Просмотр сниппета '+str(idx), 'snip': c}
    return render(request, 'pages/view_snippet.html', context)


def snippets_create(request):
    if request.method == "POST":
        form_data = request.POST
        name = form_data["name"]
        lang = form_data["lang"]
        code = form_data["code"]
        c= Snippet(name,lang,code)
        c.save()
    return redirect('snippets_list')

def create_snippet(request):
   if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("snippets_list")
       return render(request,'add_snippet.html',{'form': form})