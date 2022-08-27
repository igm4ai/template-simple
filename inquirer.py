from InquirerPy import inquirer


class NotConfirmed(Exception):
    pass


def inquire_func():
    name = inquirer.text(message="What's your name:").execute()
    age = inquirer.number(
        message="What's your age:",
        min_allowed=1,
        float_allowed=False,
        invalid_message='Age should not be less than 1.',
    ).execute()
    gender = inquirer.select(
        message="Your gender?",
        choices=["Male", "Female", "Others"],
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()

    if confirm:
        return {
            'name': name,
            'age': int(age),
            'gender': gender
        }
    else:
        raise NotConfirmed('Not comfired!')
