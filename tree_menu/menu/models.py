from django.db import models
from django.urls import reverse

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Явный урл')
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='Именованный урл')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name='Родитель')
    menu_name = models.CharField(max_length=50, verbose_name='Название меню')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        
    def get_absolute_url(self) -> str:
        if self.url:
            return self.url
        if self.named_url:
            return reverse(self.named_url)
        return "#"