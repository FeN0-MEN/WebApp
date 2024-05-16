from django import forms

class TaskForm(forms.Form):
    task_number = forms.IntegerField(label='Номер задания в ЕГЭ')
    task_count = forms.IntegerField(label='Порядковый номер задания')
    Question = forms.CharField(widget=forms.Textarea, label='Текст задания')
    Correct_Answer = forms.CharField(label='Ответ')
    Img = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://i.ibb.co/'}), label='Ссылка на картинку для задания', required=False)
    Score = forms.IntegerField(label='Количество баллов')
    HelpText = forms.CharField(widget=forms.Textarea, label='Текст подсказки')
    HelpImg= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://i.ibb.co/'}), label='Ссылка на картинку для посдказки', required=False)
    FileLink = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ссылка на файл'}), label='Ссылка на файл', required=False)