from django.shortcuts import render
from landing_page.models import Profissional


def index(request):

    dados = {
        1: {"nome": "Exame de imagem",
            "especialidade": "Ultrassonografia, raio x, tomografia, entre outros.",
            "imagem": "/assets/imagens/landing_page/exame_imagem.png"},
        2: {"nome": "Exame de sangue",
            "especialidade": "todos os tipos de exame de sangue",
            "imagem": "/assets/imagens/landing_page/exame_sangue.png"},
        3: {"nome": "Consulta médica",
            "especialidade": "diversas especialidades",
            "imagem": "/assets/imagens/landing_page/consulta_medica.png"},
        4: {"nome": "Nutricionista",
            "especialidade": "Acompanhamento nutricional, nutrição esportiva, etc",
            "imagem": "/assets/imagens/landing_page/nutricao.png"},
        5: {"nome": "Psicologia",
            "especialidade": "Consulta psicológica, Diagnóstico de TDAH, ansiedade, etc",
            "imagem": "/assets/imagens/landing_page/psicologia.png"},
        6: {"nome": "Vacinas",
            "especialidade": "Vacina da gripe, dengue, covid, entre outros",
            "imagem": "/assets/imagens/landing_page/vacina.png"}
    }

    return render(request, 'landing_page/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'landing_page/imagem.html')


def profissionais(request):

    profissionais = Profissional.objects.all()

    dados = {
        1: {"nome": "profissional 1",
            "especialidade": "Ultrassonografia, raio x, tomografia, entre outros.",
            "imagem": "/assets/imagens/landing_page/exame_imagem.png"},
        2: {"nome": "profissional 2",
            "especialidade": "todos os tipos de exame de sangue",
            "imagem": "/assets/imagens/landing_page/exame_sangue.png"},
        3: {"nome": "profissional 3",
            "especialidade": "diversas especialidades",
            "imagem": "/assets/imagens/landing_page/consulta_medica.png"},
        4: {"nome": "profissional 4",
            "especialidade": "Acompanhamento nutricional, nutrição esportiva, etc",
            "imagem": "/assets/imagens/landing_page/nutricao.png"},
        5: {"nome": "profissional 5",
            "especialidade": "Consulta psicológica, Diagnóstico de TDAH, ansiedade, etc",
            "imagem": "/assets/imagens/landing_page/psicologia.png"},
        6: {"nome": "profissional 6",
            "especialidade": "Vacina da gripe, dengue, covid, entre outros",
            "imagem": "/assets/imagens/landing_page/vacina.png"}
    }

    return render(request, 'landing_page/profissionais.html', {"cards": dados, "cardsProfissionais": profissionais})
