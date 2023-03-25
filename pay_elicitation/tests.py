from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import time

class PlayerBot(Bot):

    def play_round(self):
        time.sleep(20)  # uncomment if you want to confirm/test payoffs visually
        yield Submission(pages.FinalPayment, check_html=False)

