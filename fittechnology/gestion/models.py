from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import date


class Clasificacion(models.Model):
    codigo = models.CharField('Código',
                              max_length=25,
                              validators=[RegexValidator(regex='^[A-Z0-9-]*$', message='Solo carácteres permitidos')])
    descripcion = models.CharField('Descripción', max_length=100)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    objects = models.Manager()

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        ordering = ["descripcion"]


class DatosPersona(models.Model):

    TIPOID = [
        ('RC', 'REGISTRO CIVIL'),
        ('TI', 'TARJETA DE IDENTIDAD'),
        ('CC', 'CEDULA DE CIUDADANIA'),
        ('PA', 'PASAPORTE'),
        ('CE', 'CEDULA DE EXTRANJERIA'),
        ('PE', 'PERMISO ESPECIAL')
    ]

    SEXO = [
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    ]

    tipo_identificacion = models.CharField('Tipo de identificación', max_length=2, choices=TIPOID)
    identificacion = models.CharField('Número de identificación', max_length=25, db_index=True)
    primer_nombre = models.CharField('Primer nombre', max_length=100)
    segundo_nombre = models.CharField('Segundo nombre', max_length=100, blank=True, null=True)
    primer_apellido = models.CharField('Primer apellido', max_length=100)
    segundo_apellido = models.CharField('Segundo apellido', max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    edad = models.IntegerField('Edad', default=0, blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=2, choices=SEXO)
    peso = models.FloatField('Peso', blank=True, null=True)
    altura = models.IntegerField('Altura en centímetros', blank=True, null=True)
    imc = models.FloatField('IMC', default=0)
    es_estudiante = models.BooleanField('Es estudiante', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    objects = models.Manager()

    def calcular_edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            return today.year - self.fecha_nacimiento.year - (
                    (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        return None

    @property
    def calcular_imc(self):
        if self.peso and self.altura:
            altura_metros = self.altura / 100  # convertir altura a metros
            return round(self.peso / (altura_metros * altura_metros), 2)
        return None

    def save(self, *args, **kwargs):
        self.edad = int(self.calcular_edad())
        self.imc = self.calcular_imc
        super(DatosPersona, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.identificacion)

    class Meta:
        ordering = ["identificacion"]


