from decimal import Decimal
from django.urls import reverse
from http.client import HTTPResponse
import json
from django.shortcuts import render, redirect
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from .models import Appareil, Devis, InformationsInternaute, Panneau, Type_Panneau
# Create your views here.
class AppareilEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Appareil):
            return {
                'id': obj.pk,
                'nom': obj.nom,
                'type':obj.type,
                'cote':obj.cote,  # Ajoutez d'autres champs que vous souhaitez sérialiser
                # ...
            }
        return super().default(obj)

def WhatSysteme (total):
    result = Panneau()
    systeme = Panneau.objects.all()
    for p in systeme:
        if total <= p.cote :
            return p





def FromView(request):

    return render(request, 'coca/from.html')

class HomeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'coca/index.html')

    def post(self, request, *args, **kwargs):
        return HTTPResponse('POST request!')
    
class AppliancesView(View):
    def get(self, request, *args, **kwargs):
        appliances = Appareil.objects.all
        context = {
            'appliances':appliances
        }
        return render(request, 'coca/appliances_coca.html', context)

    def post(self, request, *args, **kwargs):
        data = []
        data_qte = []
        # nb = request.POST.get('nombre_appareil')
        for champ, valeur in request.POST.items():
            if champ.startswith('appareil-'):
                data.append(Appareil.objects.get(pk = valeur))
            if champ.startswith('qte-'):
                data_qte.append(valeur)

        total = 0
        j = 0
        appliances = []
        for i in data:
          
            total = total + (i.cote * Decimal(data_qte[j]))
            tmp = {
                'appliance':i,
                'quantity': data_qte[j],
            }
            print("------------")
            print(data_qte[j])
            appliances.append(tmp)
            j = j + 1

        result = WhatSysteme(total)
        #internaute
        internaute_json = request.session.get('internaute')
        
        if internaute_json:
            # Désérialisez l'objet JSON pour récupérer l'objet InformationsInternaute
            internaute_data = json.loads(internaute_json)
            internaute = InformationsInternaute.objects.get(id=internaute_data['internaute_id'])
        devis = Devis.objects.create(internaute_temp = internaute, total = total )
        devis = json.dumps({'devis_id': devis.id}, cls=DjangoJSONEncoder)
        appliance = json.dumps({'appliances': appliances}, cls=AppareilEncoder)
        request.session['current_devis'] = devis
        request.session['current_apps'] = appliance
        # print(request.session['current_apps'] )
        context = {
            'panneau':result,
            'types': Type_Panneau.objects.filter(panneau = result),
            'appliances': appliances,
        }
        print("************")
        print(total)

        return render(request, 'coca/result_appliance.html', context)

# A partir des factures:

class BillsView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "coca/bills_coca.html")

    def post(self, request, *args, **kwargs):
        data_qte = []
        total = 0
        cmpt = 0
        for champ, valeur in request.POST.items():
            if champ.startswith('qte-'):
                data_qte.append(valeur)
        for i in data_qte:
            total +=  int(i)
            cmpt = cmpt + 1
        moy = total / cmpt
        print(moy)

        result = WhatSysteme(moy)
       
        context = {
            'panneau':result,
            'types': Type_Panneau.objects.filter(panneau = result),
            # 'appliances': moy,
        }
        print("************")
        print(total)

        
        return render(request, 'coca/result_appliance.html', context)

def Apropos(request):

    return render(request, 'coca/apropos.html')

def Contact(request):
    
    return render(request, 'coca/contact.html')


class InfoUserView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'coca/form_user.html')

    def post(self, request, *args, **kwargs):
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        addres = request.POST.get("addres")
        mail = request.POST.get("email")
        telephone = request.POST.get("telephone")
        data = {
            'nom': nom,
            'prenom':prenom,
            'email':mail,
            'addres':addres,
            'telephone':telephone,

        }
        internaute = InformationsInternaute.objects.create(**data)
        internaute_json = json.dumps({'internaute_id': internaute.id}, cls=DjangoJSONEncoder)
        request.session['internaute'] = internaute_json
        print(internaute)
        return redirect(reverse('appliances_coca'))
class GetCoastView(View):
    def get(self, request, pk, *args, **kwargs):
        devis_json = request.session.get('current_devis')
        apps_json = request.session.get('current_apps')
        if apps_json:
            apps_data = json.loads(apps_json)

        context = {}
        if devis_json:
            # Désérialisez l'objet JSON pour récupérer l'objet InformationsInternaute
            devis_data = json.loads(devis_json)
            devis = Devis.objects.get(id=devis_data['devis_id'])
        panneau = WhatSysteme(devis.total)
        context = {
            'devis':devis,
            'panneau':panneau,
            'appliances':apps_data,
            'type': Type_Panneau.objects.filter(type = pk).first,
            }
        print()
        return render(request, 'coca/invoice.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
