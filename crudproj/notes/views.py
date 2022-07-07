from multiprocessing import context
from operator import imod, itruediv
from django.http import Http404, HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    # Notes_list contains the objects of the Notes
    Notes_list = Notes.objects.all()                     
    context = {
        'notes_list': Notes_list
    }
    return render(request,'index.html',context)

# CREATE/ADD NOTES 
def add_note(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        note =  Notes(name = name,description = description)
        note.save()
        messages.info(request,"Note is added successfully!!") 
    else:
        pass

    Notes_list = Notes.objects.all()
    context = {
        'notes_list': Notes_list
    }

    return render(request,'index.html',context)

# REMOVE/DELETE NOTES 
# myid is used for accessing a certain data in the database
def delete_note(request,my_id):                              
    note = Notes.objects.get(id = my_id)
    note.delete()
    messages.info(request,"Note is deleted successfully!!")
    return redirect(index)


# UPDATE/EDIT NOTES TRIGGER 
def edit_note(request,my_id):
    # sel_note (select-note) a variable for holding the id of the data that is being accessed
    sel_note = Notes.objects.get(id = my_id)    
    Notes_list = Notes.objects.all()
    context = {
        'sel_note':sel_note,
        'notes_list' : Notes_list
    }
    return render(request,'index.html',context)


# UPDATE/EDIT NOTES
def update_note(request,my_id):
    note = Notes.objects.get(id = my_id)
    note.name = request.POST['name']
    note.description = request.POST['description']
    note.save()
    messages.info(request,"Note is updated successfully!!")
    return redirect('index')