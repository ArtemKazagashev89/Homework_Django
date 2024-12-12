from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command("loaddata", "category.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))

        call_command("loaddata", "product.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
