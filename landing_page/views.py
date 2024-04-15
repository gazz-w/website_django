from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Exame de imagem",
            "descricao": "Ultrassonografia, raio x, tomografia, entre outros."},
        2: {"nome": "Exame de sangue",
            "descricao": "todos os tipos de exame de sangue"},
        3: {"nome": "Consulta médica",
            "descricao": "diversas especialidades"},
        4: {"nome": "Nutricionista",
            "descricao": "Acompanhamento nutricional, nutrição esportiva, etc"},
        5: {"nome": "Psicologia",
            "descricao": "Consulta psicológica, Diagnóstico de TDAH, ansiedade, etc"},
        6: {"nome": "Vacinas",
            "descricao": "Vacina da gripe, dengue, covid, entre outros"}
    }

    return render(request, 'landing_page/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'landing_page/imagem.html')
