import marvin
from marvin import ai_fn
import os
from query import manager

KEY = os.getenv("OPENAI_API_KEY")
# to use an OpenAI model (if not specified, defaults to gpt-4)
marvin.settings.openai.api_key = KEY


@ai_fn
def create_schema(
    prompt: str, faker_func_name: list[str], faked: bool = False
) -> dict | str | None:
    """
    create a schema from the prompt provided. the returned of this function
    is swagger schema like.the type is standart type for swagger. but if faked is True
    then the type is one of faker_func_name.
    """


def main(event, context):
    prompt = event.get("prompt")
    query = manager.table.select("function_name").execute()
    schema = create_schema(prompt, [i["function_name"] for i in query.data], faked=True)
    if isinstance(schema, dict):
        return {
            "statusCode": 200,
            "body": {
                "data": schema,
            },
        }
    return {
        "statusCode": 400,
        "body": {
            "data": {
                "message": "failed to create schema",
                "prompt": prompt,
            }
        },
    }
