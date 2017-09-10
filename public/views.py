from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'public/index.html')


def contact(request):
    contents = [
        'You can contact me through e-mail, whatsapp, twitter, instagram',
        'my email is javafolabi@gmail.com, VictorIAfolabi1, victor_iyiola'
    ]
    return render(request, 'public/pages.html', {'contents': contents})
