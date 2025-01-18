from django import forms
from .models import Product
from django.core.exceptions import ValidationError

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "is_active",
            "image",
            "category",
            "price",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["is_active"].widget.attrs.update(
            {
                "class": "form-check-input",
            }
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите стоимость продукта"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError('Вы используете запретное слово в названии продукта: "{}"'.format(word))

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError('Вы используете запретное слово в описании продукта: "{}"'.format(word))
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price
