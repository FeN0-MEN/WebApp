from django.db import models

class Task(models.Model):
    task_number = models.IntegerField()
    task_text = models.TextField()
    answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    # Добавьте остальные поля согласно вашим требованиям

    def __str__(self):
        return f'Задание {self.task_number}'
