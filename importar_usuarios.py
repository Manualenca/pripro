import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pripro.settings")
django.setup()

from mae.models import Auditor, Ficha

auditor = Auditor.objects.create(nombre='Ariel', apellido='Ramos')
auditor.save()

#ficha = Ficha.objects.create(auditor=auditor)


