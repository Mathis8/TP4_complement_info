from email.message import Message
from pprint import pprint


from InquirerPy.validator import PasswordValidator
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session
from business_object.user import User


ASK_FIRST_NAME=inquirer.text(message = 'What\'s your first name')
ASK_LAST_NAME=inquirer.text(message = 'What\'s your last name')
ASK_PSEUDO=inquirer.text(message = 'What\'s your pseudo')
ASK_PASSWORD=inquirer.secret(message='What\'s your password.'
        ,validate=PasswordValidator(length=8, cap=True, special=True, number=True),
        transformer=lambda _: "[hidden]",
        long_instruction="Password require length of 8, 1 cap char, 1 special char and 1 number char.",)


class SignInExample(AbstractView):


    def display_info(self):
        print(f"Account creation")

    def make_choice(self):
        first_name = ASK_FIRST_NAME.execute()
        last_name = ASK_LAST_NAME.execute()
        pseudo = ASK_PSEUDO.execute()
        password =ASK_PASSWORD.execute()
        user = User(first_name = first_name
            ,last_name = last_name
            ,pseudo = pseudo
            ,password = password
        )
        print(user)
        Session().user_mdp = user.password
        Session().user_name = user.pseudo
        from view.start_view import StartView
        return StartView()
