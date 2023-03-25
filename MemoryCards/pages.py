from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random



class Instructions(Page):
    pass


class Observation(Page):
    timeout_seconds = Constants.time


class Report(Page):
    form_model = 'player'
    form_fields = ['report_first', 'report_second', 'report_third', 'report_fourth', 'report_fifth', 'report_sixth', 'report_seventh', 'report_eighth', 'report_ninth', 'report_tenth', 'report_eleventh', 'report_twelfth',
                   'report_thirteenth', 'report_fourteenth', 'report_fifteenth', 'report_sixteenth', 'report_seventeenth', 'report_eighteenth', 'report_nineteenth', 'report_twentieth']


class Guess(Page):
    form_model = 'player'
    form_fields = ['guess_yours', 'guess_average']

    def  before_next_page(self):
        self.player.get_check_first()
        self.player.get_check_second()
        self.player.get_check_third()
        self.player.get_check_fourth()
        self.player.get_check_fifth()
        self.player.get_check_sixth()
        self.player.get_check_seventh()
        self.player.get_check_eighth()
        self.player.get_check_ninth()
        self.player.get_check_tenth()
        self.player.get_check_eleventh()
        self.player.get_check_twelfth()
        self.player.get_check_thirteenth()
        self.player.get_check_fourteenth()
        self.player.get_check_fifteenth()
        self.player.get_check_sixteenth()
        self.player.get_check_seventeenth()
        self.player.get_check_eighteenth()
        self.player.get_check_nineteenth()
        self.player.get_check_twentieth()
        self.player.get_correct()
        self.player.round_payoff = 0.25*self.player.correct
        print(self.player.correct)



class Wait(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
        average = self.group.average
        for p in self.group.get_players():
            if p.guess_yours == p.correct:
                p.round_payoff += 1
            else:
                p.round_payoff = p.round_payoff
            if abs(p.guess_average - average) <= 0.5:
                p.round_payoff += 1
            else:
                p.round_payoff = p.round_payoff
            print(p.round_payoff)


class Results(Page):
    def vars_for_template(self):
        self.participant.payoff += self.player.round_payoff
        print(self.participant.payoff)




page_sequence = [Instructions, Observation, Report, Guess, Wait, Results]
