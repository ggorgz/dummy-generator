from builder import build_schema


def main(event, context):
    schema = event.get("schema")
    properties = schema.get("properties", {})

    return {
        "statusCode": 200,
        "body": {
            "data": build_schema(properties),
        },
    }
