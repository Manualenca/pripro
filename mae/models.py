from django.db import models
import datetime
from django.db.models.query import QuerySet


# Disable items instead delete
class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(activo=False)


class ActiveManager(models.Manager):
    def activo(self):
        return self.model.objects.filter(activo=True)


    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)



class Auditor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    activo = models.BooleanField(default=True, editable=False)

    objects = ActiveManager()


    class Meta:
        verbose_name_plural = 'Auditores'


    def __str__(self):
        return '{}, {}'.format(self.nombre, self.apellido)



class Efector(models.Model):
    nombre = models.CharField(max_length=200)
    cuie = models.CharField(max_length=5)
    activo = models.BooleanField(default=True, editable=False)

    objects = ActiveManager()


    class Meta:
        verbose_name_plural = 'Efectores'

    def __str__(self):
        return '{}, {}'.format(self.cuie, self.nombre)

MESES = (
    (1, 'Enero'),
    (2, 'Febrero')
)


class Periodo(models.Model):
    mes = models.IntegerField(choices=MESES)
    anio = models.IntegerField("Año")
    activo = models.BooleanField(default=True, editable=False)

    objects = ActiveManager()
    
    
    class Meta:
        ordering = ['-anio', '-mes']
        verbose_name_plural = 'Periodo'

    def __str__(self):
        return '{}-{}'.format(self.mes, self.anio)


class Ficha(models.Model):
    auditor = models.ForeignKey('Auditor', on_delete=models.CASCADE)
    efector = models.ForeignKey('Efector', on_delete=models.CASCADE)
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    # fecha_fin 
    fecha_creacion = models.DateField(auto_now_add=True, editable=False)
    activo = models.BooleanField(default=True, editable=False)

    objects = ActiveManager()


    class Meta:
        verbose_name_plural = 'Fichas'

    def __str__(self):
        return '{}: {}'.format(self.fecha_inicio, self.auditor, self.efector)


