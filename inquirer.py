from InquirerPy import inquirer

from igm.conf import InquireRestart

_LAST_NAME = ""
_LAST_AGE = 18
_LAST_GENDER = "Male"


def inquire_func():
    global _LAST_AGE, _LAST_NAME, _LAST_GENDER

    name = inquirer.text(message="What's your name:", default=_LAST_NAME).execute()
    age = int(inquirer.number(
        message="What's your age:",
        min_allowed=1,
        float_allowed=False,
        invalid_message='Age should not be less than 1.',
        default=_LAST_AGE,
    ).execute())
    gender = inquirer.select(
        message="Your gender?",
        choices=["Male", "Female", "Others"],
        default=_LAST_GENDER,
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()

    if confirm:
        return {
            'name': name,
            'age': age,
            'gender': gender
        }
    else:
        # save this time's fillings
        _LAST_NAME = name
        _LAST_AGE = age
        _LAST_GENDER = gender
        raise InquireRestart('Not confirmed.')
