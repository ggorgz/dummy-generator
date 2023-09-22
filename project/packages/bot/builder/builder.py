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
        if not value["type"]:
            data[key] = None
            continue

        # if type is object, run recursively
        if value["type"] == "object" and "properties" in value:
            data[key] = build_schema(value["properties"])
            continue

        data[key] = generate(value["type"])

    return data


def generate(data_type: str) -> any | None:
    if hasattr(fake, data_type):
        func = getattr(fake, data_type)
        return func()

    match data_type:
        case "string" | "str":
            return fake.pystr()
        case "number" | "int":
            return fake.pyint()
        case "boolean" | "bool":
            return fake.pybool()
