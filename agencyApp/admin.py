from django.contrib import admin
from .models.user import User
from .models.purchase import Purchase
from .models.pack import Pack

admin.site.register(User)
admin.site.register(Purchase)
admin.site.register(Pack)
