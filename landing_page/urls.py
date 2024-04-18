from django.urls import path
from landing_page.views import index, imagem, profissionais

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('profissionais/', profissionais, name='profissionais')

]
