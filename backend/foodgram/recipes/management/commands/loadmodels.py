import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        file_path = options["path"]

        with open(file_path, encoding='utf-8') as f:
            jsondata = json.load(f)
            if 'color' in jsondata[0]:
                for line in jsondata:
                    if not Tag.objects.filter(
                       slug=line['slug']).exists():
                        Tag.objects.create(
                            name=line['name'],
                            color=line['color'],
                            slug=line['slug'],
                        )
            elif 'measurement_unit' in jsondata[0]:
                for line in jsondata:
                    if not Ingredient.objects.filter(
                       name=line['name'],
                       measurement_unit=line['measurement_unit']).exists():
                        Ingredient.objects.create(
                            name=line['name'],
                            measurement_unit=line['measurement_unit']
                        )
