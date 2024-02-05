from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView

class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    success_url = reverse_lazy("dashboard:dashboard")


class MyPasswordSetView(LoginRequiredMixin,PasswordSetView):
    success_url = reverse_lazy("dashboard:dashboard")