from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json
import requests
from django.shortcuts import render, redirect
from .forms import TaskForm

# URL адреса для взаимодействия с Firebase
database_url = "https://appbase-66912-default-rtdb.europe-west1.firebasedatabase.app/"
storage_url = "https://firebasestorage.googleapis.com/v0/b/appbase-66912.appspot.com/o"


def upload_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = {
                "Question": form.cleaned_data['Question'],
                "Correct_Answer": form.cleaned_data['Correct_Answer'],
                "Score": form.cleaned_data['Score'],
                "HelpText": form.cleaned_data['HelpText'],
            }

            # Проверка и считывание ссылки на изображение задания
            image_link = form.cleaned_data['Img']
            task_data["Img"] = image_link

            # Проверка и считывание ссылки на изображение подсказки
            help_image_link = form.cleaned_data['HelpImg']
            task_data["HelpImg"] = help_image_link

            # Проверка и считывание ссылки на файл
            file_link = form.cleaned_data['FileLink']
            task_data["FileLink"] = file_link

            # Определение папки для задания в Firebase
            task_folder = f"Task_{form.cleaned_data['task_number']}"
            task_subfolder = f"Number_{form.cleaned_data['task_count']}"
            response = requests.put(f"{database_url}/{task_folder}/{task_subfolder}.json", json=task_data)
            if response.status_code == 200:
                return redirect('sucess')
    else:
        form = TaskForm()
    return render(request, 'upload_task.html', {'form': form})

def sucess(request):
    return render(request, 'sucess.html')
