from django.urls import path
from django.views.generic import TemplateView


# тестовое представление
view = TemplateView.as_view(template_name='menu/index.html')

# тестовые урлы
urlpatterns = [
    path('', view, name='index'),
    path('kategoriya-1-2/', view, name='kategoriya-1-2'), 
    path('kategoriya-2-2/', view, name='kategoriya-2-2'),
    path('kategoriya-3-2/', view, name='kategoriya-3-2'),
    path('kategoriya-4-2/', view, name='kategoriya-4-2'),
    path('kategoriya-5-2/', view, name='kategoriya-5-2'),
    path('kategoriya-6-2/', view, name='kategoriya-6-2'),
    path('kategoriya-1-1/', view, name='kategoriya-1-1'),
    path('kategoriya-2-1/', view, name='kategoriya-2-1'),
    path('kategoriya-3-1/', view, name='kategoriya-3-1'),
    path('kategoriya-4-1/', view, name='kategoriya-4-1'),
    path('kategoriya-5-1/', view, name='kategoriya-3-1'),
    path('kategoriya-6-1/', view, name='kategoriya-4-1'),
]
