from django.urls import path
from .views import upload_task, sucess

urlpatterns = [
    path('upload/', upload_task, name='upload_task'),
    path('sucess/', sucess, name='sucess')
]