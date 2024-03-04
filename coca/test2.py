from django.test import TestCase, RequestFactory
from .views import checkUser
from .models import InformationsInternaute
from django.urls import reverse
import json

class CheckUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_check_user_exists(self):
        # Créer un utilisateur factice pour le test
        email = "mbodapson@gmail.com"
        nom = "soul"
        prenom = "bodapson"
        telephone = "696264793"
        addres = "Yaounde"
        InformationsInternaute.objects.create(nom = nom, prenom = prenom,email=email, addres = addres, telephone = telephone)

        url = reverse('check_user')  # Assurez-vous de remplacer 'check_user' par le nom réel de votre URL
        response = self.client.post(url, {'email': email})

        # Vérifier que la réponse a un code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Analyser les données JSON de la réponse
        response_data = json.loads(response.content)

        print(response_data)
        # Vérifier si la réponse contient "yes"
        if response_data['result'] =='yes':
            print("Yes")
        else:
            print("*******")
            print("NO")
            