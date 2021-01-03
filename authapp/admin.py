from django.contrib import admin
from authapp.models import Person, Address, Counteragent, PhoneNumber, City, Country, Weather

# Register your models here.

admin.site.register(PhoneNumber)
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Counteragent)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Weather)
