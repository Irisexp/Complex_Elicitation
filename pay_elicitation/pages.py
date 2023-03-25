from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class FinalPaymentWaitPage(WaitPage):
    def after_all_players_arrive(self):
        # random.seed(random.randint(1, 999))
        rounds_to_pay =  [random.randint(1,4)]
        print('rounds_to_pay')
        print(rounds_to_pay)
        apps_to_pay = random.choices([0, 1, 2], weights=[1/3, 1/3, 1/3])[0]
        paylist = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
        random_pay = random.choices(paylist, k=1)[0]
        print('random_pay')
        print(random_pay)
        print('draw')
        print(apps_to_pay)
        for p in self.group.get_players():
            print('id')
            print(p.id_in_group)
            print('choice')
            choice = p.participant.vars['choice']
            print(choice)
            print('wtp')
            wtp = p.participant.vars['pay']
            print(wtp)
            if apps_to_pay < 2:
                apps_to_pay = apps_to_pay
            elif choice == 0 and wtp <= random_pay:
                apps_to_pay = 3
                p.payoff += random_pay
            elif choice == 0 and wtp > random_pay:
                apps_to_pay = 2
            elif choice == 1 and wtp <= random_pay:
                apps_to_pay = 2
                p.payoff += random_pay
            else:
                apps_to_pay = 3
            print(apps_to_pay)
            payoff_list = p.participant.vars.get('payoffs', [])
            print('payoff')
            print(payoff_list)
            p.participant.vars['app_display_list'] = [apps_to_pay]
            round_list = p.participant.vars.get('rounds_display_list', [])
            round_list.append(rounds_to_pay)
            # print(rounds_to_pay)
            p.participant.vars['rounds_display_list'] = round_list
            # now saving to otree's payoff variable for currency calculations
            p.payoff += payoff_list[apps_to_pay][rounds_to_pay[0]]
            print('payoff')
            print(p.payoff)


class FinalPayment(Page):
    def vars_for_template(self):
        apps_list = self.player.participant.vars.get('app_display_list', [])
        rounds_list = self.player.participant.vars.get('rounds_display_list', [])
        payoff_list = self.player.participant.vars.get('payoffs', [])

        # django_display_list = []
        # for i in range(len(apps_list)):
        #     a_list = [apps_list[i]+1]  # we need to add 1 so that apps and rounds line up with a 1 instead of 0 index
        #     a_list.append([r+1 for r in rounds_list[i]])
        #     temp_list = []
        #     for r in rounds_list[i]:
        #         temp_list.append(int(payoff_list[apps_list[i]][r]))
        #     # a_list.append(payoff_list[apps_list[i]][rounds_list[i]])
        #     a_list.append(temp_list)
        #     django_display_list.append(a_list)

        dollars = self.participant.payoff_plus_participation_fee()
        self.player.dollars = dollars

        return dict(round= round, dollars=dollars)


page_sequence = [
    FinalPaymentWaitPage,
    FinalPayment,
]


