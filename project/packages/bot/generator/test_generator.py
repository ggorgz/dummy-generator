from project.packages.bot.generator.__main__ import main


def test_generator():
    response = main(
        {"prompt": "create a user schema that have age, name, phone number, gender"},
        None,
    )
    print(response)
