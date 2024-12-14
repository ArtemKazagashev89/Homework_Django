from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категории", help_text="Введите наименование категории"
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта", blank=True, null=True
    )
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену за покупку")
    created_at = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category", "name", "price"]