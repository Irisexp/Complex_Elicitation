from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Instruction(Page):
    pass


class Choice(Page):
    form_model = "player"
    form_fields = ["card_choice"]

class WTP(Page):
    form_model = "player"
    form_fields = ["wtp"]


class Waitforall(WaitPage):
    def after_all_players_arrive(self):
        choicelist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
        number = random.choices(choicelist, k=1)[0]
        print(number)
        blue = random.choices([1, 4, 5], k=1)[0]
        print(blue)
        for p in self.group.get_players():
            p.number = number
            p.blue = blue
            print(p.card_choice)
            if p.card_choice == 1:
                if p.wtp <= p.number:
                    p.round_payoff = blue + number
                    p.prefer = 1
                else:
                    p.round_payoff = 4
                    p.prefer = 0
            else:
                if p.wtp <= p.number:
                    p.round_payoff = 4 + number
                    p.prefer = 1
                else:
                    p.round_payoff = blue
                    p.prefer = 0


class Results(Page):
    def vars_for_template(self):
        self.participant.payoff += self.player.round_payoff
        print(self.participant.payoff)
        question = 10*self.player.number
        return dict(question = question)

page_sequence = [Choice, WTP, Waitforall, Results]
