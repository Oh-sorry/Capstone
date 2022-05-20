from django.contrib import admin

# Register your models here.

from test_app.models import Test

admin.site.register(Test)
# admin.site.register(Account)