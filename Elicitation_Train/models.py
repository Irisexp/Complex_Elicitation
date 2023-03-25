from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Junya Zhou'
doc = """
Elicitation of preferences for complexity
"""


class Constants(BaseConstants):
    name_in_url = 'Elicitation_Train'
    players_per_group = None
    num_rounds = 1
    # cost = c(4)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_payoff = models.CurrencyField()

    prefer = models.IntegerField()

    wtp = models.FloatField(
        label='Please enter a number you would like to switch between 0.1 and 2', choices = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2],
    min=0.1, max=3)

    number = models.FloatField()

    blue = models.IntegerField()

    card_choice = models.IntegerField(
        choices=[
            [1, 'Red Card'],
            [2, 'Blue Card'],
        ],
        label='',
        widget=widgets.RadioSelect,
    )

