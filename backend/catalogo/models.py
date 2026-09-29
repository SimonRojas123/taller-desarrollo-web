from django.db import models

# Create your models here.

class Servicio(models.Model):
    """Servicio que ofrece el negocio (ejemplo; adáptalo a tu proyecto)."""

    nombre = models.CharField(max_length=100)  # texto corto
    descripcion = models.TextField(blank=True)  # texto largo, opcional
    precio = models.DecimalField(
        max_digits=10, decimal_places=0
    )  # CLP no usa decimales
    activo = models.BooleanField(default=True)  # visible u oculto
    creado_en = models.DateTimeField(auto_now_add=True)  # se llena solo al crear

    class Meta:
        ordering = ["nombre"]  # orden por defecto de las consultas
        verbose_name_plural = "servicios"  # cómo se ve en el admin

    def __str__(self):
        # Texto que Django muestra cuando imprime el objeto (admin, shell)
        return self.nombre
