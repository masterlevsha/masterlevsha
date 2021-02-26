from django.shortcuts import render


def index(request):
    return render(request, 'tehnikaapp/index.html')


def remont_televizorov(request):
    return render(request, 'tehnikaapp/remont_televizorov.html')


def remont_stiralnyh_mashin(request):
    return render(request, 'tehnikaapp/remont_stiralnyh_mashin.html')


def remont_posudomoechnyh_mashin(request):
    return render(request, 'tehnikaapp/remont_posudomoechnyh_mashin.html')


def remont_holodilnikov(request):
    return render(request, 'tehnikaapp/remont_holodilnikov.html')


def remont_kofemashin(request):
    return render(request, 'tehnikaapp/remont_kofemashin.html')


def remont_ehlektroplit(request):
    return render(request, 'tehnikaapp/remont_ehlektroplit.html')


def remont_varochnyh_panelej(request):
    return render(request, 'tehnikaapp/remont_varochnyh_panelej.html')


def remont_duhovyh_shkafov(request):
    return render(request, 'tehnikaapp/remont_duhovyh_shkafov.html')


def remont_mikrovolnovok(request):
    return render(request, 'tehnikaapp/remont_mikrovolnovok.html')
