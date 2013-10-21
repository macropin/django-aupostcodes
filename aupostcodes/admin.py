from django.contrib import admin

from models import AUPostalArea, AUPostCode

class AUPostalAreaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'postcode', 'locality', 'state')

admin.site.register(AUPostalArea, AUPostalAreaAdmin)
admin.site.register(AUPostCode)

