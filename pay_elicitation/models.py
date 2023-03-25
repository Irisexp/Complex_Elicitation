from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Junya'

doc = """
Randomly choosing one round for final payoff
"""


class Constants(BaseConstants):
    name_in_url = 'pay_elicitation'
    players_per_group = None
    num_rounds = 1

    num_apps_to_pay = 1  # of the apps played, how many do you want to pay out

    num_rounds_to_pay = 1  # for each app, how many rounds of that app to pay


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    dollars = models.CurrencyField()
