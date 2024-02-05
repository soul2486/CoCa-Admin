# Register your models here.
from django.contrib import admin

from coca.models import Appareil, Panneau, Type_Panneau, TypePanneau

# Register your models here.
# Appareil模型的管理器
@admin.register(Appareil)
class AppareilAdmin(admin.ModelAdmin):
    list_display = ["nom", "type", "cote"]
    search_fields = ["nom"]
    list_filter =[]
@admin.register(Panneau)
class PanneauAdmin(admin.ModelAdmin):
    list_display = ["nom", "PV", "cote"]
    search_fields = ["nom"]
    list_filter =[]

@admin.register(TypePanneau)
class TypePanneauAdmin(admin.ModelAdmin):
    list_display = ["type",]
    search_fields = [""]
    list_filter =[]

@admin.register(Type_Panneau)
class Type_PanneauAdmin(admin.ModelAdmin):
    list_display = ["panneau", "type", "prix"]
    search_fields = [""]
    list_filter =[]

