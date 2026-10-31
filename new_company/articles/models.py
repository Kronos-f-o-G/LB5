from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    # Название маршрута (как title в примере)
    title = models.CharField(max_length=200, verbose_name="Название маршрута")
    # Автор записи (как в примере)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Оформил")
    # Текст с описанием перевозки (водители, расстояние, даты и т.д.)
    text = models.TextField(verbose_name="Детали перевозки")
    # Дата создания записи (автоматически)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text

    class Meta:
        verbose_name = "Перевозка"
        verbose_name_plural = "Перевозки"