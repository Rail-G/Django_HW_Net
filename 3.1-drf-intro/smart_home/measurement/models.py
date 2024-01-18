from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя датчика')
    description = models.CharField(max_length=200, verbose_name='Описание датчика')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'датчик'
        verbose_name_plural = 'датчики'

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='mesaurement', verbose_name='Датчик')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    photo = models.ImageField(blank=True, verbose_name='Фото')

    def __str__(self):
        return str(self.temperature)
    
    class Meta:
        ordering = ['sensor_id', 'date']
        verbose_name = 'измерения'
        verbose_name_plural = 'измерении'