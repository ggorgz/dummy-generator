from django.core.management.base import BaseCommand
from core.resources.models import FakeFunctionsData
from django.utils import timezone
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("fixtures/provider_schema.json", "r") as fjson:
            data = json.loads(fjson.read())
            list_of_data = data["faker_collection"]
            now = timezone.now()
            fake_functions_data = [
                {**item, "created_at": now, "updated_at": now} for item in list_of_data
            ]
            FakeFunctionsData.objects.bulk_create(
                [FakeFunctionsData(**item) for item in fake_functions_data]
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully created {} FakeFunctionsData instances.".format(
                        len(fake_functions_data)
                    )
                )
            )
