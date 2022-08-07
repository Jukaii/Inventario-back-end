from django.contrib import admin
from .models.user import User
from .models.rol import Rol

admin.site.register(User)
admin.site.register(Rol)