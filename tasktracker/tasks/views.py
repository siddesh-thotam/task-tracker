from django.shortcuts import render
from tasks.models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            title = request.POST.get("title")
            description = request.POST.get("description")

            Tasks.objects.create(
                title = title,
                description = description
            )


            messages.success(request , "Task Created Successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            title = request.POST.get("title")
            description = request.POST.get("description")

            update_task = Tasks.objects.get(id=id)
            update_task.title = title
            update_task.description = description

            update_task.save()

            messages.success(request , "Task Updated Successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Tasks.objects.get(id=id).delete()

            messages.success(request , "Task Deleted Successfully")

        elif "search" in request.POST:
            query = request.POST.get("querysearch")
            tasks = Tasks.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))


    context={'tasks':tasks, "query":query}
    return render(request,'tasks/index.html',context=context)

