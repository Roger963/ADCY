from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from django.contrib import messages
from .models import Hospital


def hospitales(request):
    posts = Hospital.objects.all()
    return render(request, 'hospitales.html', {
        'hostpitales': hospitales
    })


def create(request):
    if request.POST:
        req = request.POST
        post = Posts(title=req.get('title'), slug=slugify(req.get('title')), content=req.get('content'))
        post.save()
        messages.success(request, 'The record was saved successfully')
        return redirect('/')
    else:
        return render(request, 'create.html')

def update(request, medico):
    return render(request, 'update.html')

def read(request, medico):
    return render(request, 'detail.html')

def delete(request, post_id):
    post = Medico.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'The record was deleted successfully')
    return redirect('/')
