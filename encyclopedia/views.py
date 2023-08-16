from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from . import util
import random
import markdown2

def convertToHtml(title):
    content = util.get_entry(title)
    html_docs = markdown2.Markdown()
    if content == None:
        return None
    else:
        return html_docs.convert(content)
    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def info(request,title):
    if title not in util.list_entries():
        return render(request,"encyclopedia/error.html",{'message' : 'Error'})
    return render(request, "encyclopedia/entries.html", {"docs": convertToHtml(title), 'title':title})

def search(request):
    searched = request.POST['q']
    substring = []
    names = util.list_entries()
    print(searched)
    if searched in names:
        params = {'title':searched, 'docs':convertToHtml(searched)}
        return render(request,"encyclopedia/search.html", params )
    elif (searched not in names):
        for i in range(len(names)):
            if searched in names[i]:
                substring.append(names[i])
                return render(request, "encyclopedia/list.html", {'list':substring})
            elif i == len(names)-1:
                return render(request,"encyclopedia/error.html", {'message':'The title you have searched does not exists'})
def NewPage(request):
    return render(request, "encyclopedia/Newpage.html")

def save(request):
    title = request.POST['title']
    content = request.POST['text']
    names =  util.list_entries()
    if title not in names:
        util.save_entry(title, content)
        params = {'title': title, 'content':convertToHtml(title)}
        return render(request, "encyclopedia/save.html", params)
    elif title in names:
        return render(request,"encyclopedia/error.html", {'message':'The title you entered already exists'} )
    
def edit_page(request, title):
    return render(request, "encyclopedia/edit.html", {'title':title, 'content':util.get_entry(title)})

def save_edit(request, title):
    content = request.POST['text_edit']
    util.save_entry(title, content)
    params = {'title':title, 'content':convertToHtml(title)}
    return render(request, "encyclopedia/save_edit.html", params)

def RandomPage(request):
    names =  util.list_entries()
    rand = random.sample(names,1)
    params = {'title':rand[0], 'content':convertToHtml(rand[0])}
    return render(request, "encyclopedia/RandomPage.html",params)


    




    
    
       
        



    
    

