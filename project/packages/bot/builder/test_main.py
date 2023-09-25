from project.packages.bot.builder.__main__ import main


def test_main():
    data = main(
        {
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "name"},
                    "phone number": {"type": "phone_number"},
                    "gender": {"type": "passport_gender"},
                },
            }
        },
        None,
    )
    assert data["statusCode"] == 200
