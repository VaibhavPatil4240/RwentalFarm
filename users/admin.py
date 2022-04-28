
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from users.models import Account
from django.contrib.auth.models import User
class AccountInLine(admin.StackedInline):
    model=Account
    can_delete=False
    verbose_name_plural='Accounts'

class CustomizeUserAdmin(UserAdmin):
    inlines=(AccountInLine,)

admin.site.unregister(User)
admin.site.register(User,CustomizeUserAdmin)    

admin.site.register(Account)