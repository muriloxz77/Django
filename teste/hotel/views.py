from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, cadastro
from .forms import CheckinForm


def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, "homepage.html", context)


def quartos(request):
    context = {}
    dados_quartos = quarto.objects.all()
    context["dados_quartos"] = dados_quartos
    return render(request, "quartos.html", context)


def checkin(request):
    if request.method == "POST":
        form = CheckinForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            sobre_nome = form.cleaned_data["sobrenome"]
            email = form.cleaned_data["email"]
            tipo_quarto = form.cleaned_data["tipo_quarto"]
            data_reserva = form.cleaned_data["data_reserva"]
            checkin = cadastro(
                nome=nome,
                email=email,
                tipo_quarto=tipo_quarto,
                data_reserva=data_reserva,
                sobrenome=sobre_nome,
            )
            checkin.save()

            return HttpResponse("Checkin realizado com sucesso!")
    else:
        form = CheckinForm()
    return render(request, "checkin.html", {"form": form})
