from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Contract, Event


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'company_name')

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'client')


admin.site.register(Contract, ContractAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Event)