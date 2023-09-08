import faker
from faker_music import MusicProvider
from faker_vehicle import VehicleProvider
from faker_marketdata import MarketDataProvider
# from query import manager

fake = faker.Faker()
fake.add_provider(MusicProvider)
fake.add_provider(VehicleProvider)
fake.add_provider(MarketDataProvider)


def main(event, context):
    schema = event.get("schema")
    properties = schema.get("properties", {})
    data = {}
    for key, value in properties.items():
        if hasattr(fake, value["type"]):
            func = getattr(fake, value["type"])
            data[key] = func()
        else:
            if value["type"] == "string":
                data[key] = fake.pystr()
            elif value["type"] == "number":
                data[key] = fake.pyint()
            elif value["type"] == "boolean":
                data[key] = fake.pybool()
    return {
        "statusCode": 200,
        "body": {
            "data": data,
        },
    }
