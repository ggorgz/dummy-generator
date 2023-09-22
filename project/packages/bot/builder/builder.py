import faker
from faker_music import MusicProvider
from faker_vehicle import VehicleProvider
from faker_marketdata import MarketDataProvider


fake: faker.Faker = faker.Faker()
fake.add_provider(MusicProvider)
fake.add_provider(VehicleProvider)
fake.add_provider(MarketDataProvider)


def build_schema(properties: dict) -> dict:
    data = {}

    for key, value in properties.items():
        # if type is not defined
        if not (data_type := value.get("type")):
            data[key] = None
            continue

        # if type is object, run recursively
        if data_type == "object" and "properties" in value:
            data[key] = build_schema(value["properties"])
            continue

        # if type is of faker type
        if hasattr(fake, data_type):
            func = getattr(fake, data_type)
            data[key] = func()
            continue

        # if type is custom defined
        if data_type in ["string", "number", "boolean"]:
            data[key] = value.get("value")
            continue

        # otherwise use default value, or None
        data[key] = value.get("default")

    return data
