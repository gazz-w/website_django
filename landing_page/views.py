from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Exame de imagem",
            "descricao": "Ultrassonografia, raio x, tomografia, entre outros.",
            "imagem": "/assets/imagens/landing_page/exame_imagem.png"},
        2: {"nome": "Exame de sangue",
            "descricao": "todos os tipos de exame de sangue",
            "imagem": "/assets/imagens/landing_page/exame_sangue.png"},
        3: {"nome": "Consulta médica",
            "descricao": "diversas especialidades",
            "imagem": "/assets/imagens/landing_page/consulta_medica.png"},
        4: {"nome": "Nutricionista",
            "descricao": "Acompanhamento nutricional, nutrição esportiva, etc",
            "imagem": "/assets/imagens/landing_page/nutricao.png"},
        5: {"nome": "Psicologia",
            "descricao": "Consulta psicológica, Diagnóstico de TDAH, ansiedade, etc",
            "imagem": "/assets/imagens/landing_page/psicologia.png"},
        6: {"nome": "Vacinas",
            "descricao": "Vacina da gripe, dengue, covid, entre outros",
            "imagem": "/assets/imagens/landing_page/vacina.png"}
    }

    return render(request, 'landing_page/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'landing_page/imagem.html')
