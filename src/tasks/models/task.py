from django.db import models
from django.urls import reverse
from .type import Type
from datetime import datetime
from ckeditor.fields import RichTextField

class Task(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200)
    description = RichTextField(verbose_name='Описание', null=True, blank=True, max_length=2000)
    status = models.ForeignKey(verbose_name='Статус', to='tasks.Status', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    types = models.ManyToManyField(Type, related_name='tasks')

    def __str__(self):
        return self.summary
    
    def get_detail_url(self):
        return reverse('task-detail', kwargs={'pk':self.id})
    
    def get_update_url(self):
        return reverse('task-update', kwargs={'pk':self.id})
    
    def get_delete_url(self):
        return reverse('task-delete', kwargs={'pk':self.id})

    def get_date(self):
        time = datetime.now()
        if self.updated_at.day == time.day:
            return str(time.hour - self.updated_at.hour) + " часа назад"
        else:
            if self.updated_at.month == time.month:
                return str(time.day - self.updated_at.day) + " дня назад"
            else:
                if self.updated_at.year == time.year:
                    return str(time.month - self.updated_at.month) + " месяца назад"
        return self.updated_at
