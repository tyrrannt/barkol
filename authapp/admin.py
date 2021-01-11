from django.contrib import admin
from authapp.models import Person, Address, Counteragent, PhoneNumber, City, Country, Weather, Job, Work

# Register your models here.

admin.site.register(PhoneNumber)
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Counteragent)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Weather)
admin.site.register(Work)
admin.site.register(Job)
