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
import copy
import itertools

author = 'Junya Zhou'

doc = """
5 simple rounds after elicitation
"""


class Constants(BaseConstants):
    name_in_url = 'Simple_After'
    players_per_group = 2
    num_rounds = 5
    time = 15


# if this number changes, the following dim_ report should also change

    initial_prior = 1/3
    sender_payoffs = [c(15), c(12), c(3)]
    receiver_payoffs = [c(15), c(12), c(8), c(3)]

class Subsession(BaseSubsession):

#The code is working, for each round, the profiles are randomly drawn.
    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)

        Simple_Up_sixth = [7, 8, 7]

        Simple_Middle_sixth = [8, 9, 9]

        Simple_Down_sixth = [9, 7, 8]

        Simple_Up_seventh = [2, 1, 3]

        Simple_Middle_seventh = [1, 2, 2]

        Simple_Down_seventh = [3, 3, 1]

        Simple_Up_eighth = [6, 4, 5]

        Simple_Middle_eighth = [5, 6, 6]

        Simple_Down_eighth = [4, 5, 4]

        Simple_Up_ninth = [8, 9, 9]

        Simple_Middle_ninth = [9, 7, 8]

        Simple_Down_ninth = [7, 8, 7]
#second sets

        Simple_Up_tenth = [12, 12, 10]

        Simple_Middle_tenth = [10, 11, 12]

        Simple_Down_tenth = [11, 10, 11]


        self.session.vars['Simple_Up'] = [Simple_Up_sixth, Simple_Up_seventh, Simple_Up_eighth, Simple_Up_ninth, Simple_Up_tenth]
        self.session.vars['Simple_Middle'] = [Simple_Middle_sixth, Simple_Middle_seventh, Simple_Middle_eighth, Simple_Middle_ninth, Simple_Middle_tenth]
        self.session.vars['Simple_Down'] = [Simple_Down_sixth, Simple_Down_seventh, Simple_Down_eighth, Simple_Down_ninth, Simple_Down_tenth]



class Group(BaseGroup):

    true_state = models.IntegerField(label="")

    profile_num = models.IntegerField(label="")
    #
    # random_first = models.IntegerField(label="The first question is:")
    #
    # random_second = models.IntegerField(label="The second question is:")
    #
    # random_third = models.IntegerField(label="The third question is:")

    attribute_first = models.IntegerField(label="")

    attribute_second = models.IntegerField(label="")

    attribute_third = models.IntegerField(label="")

    report_first = models.IntegerField(label="")

    report_second = models.IntegerField(label="")

    report_third = models.IntegerField(label="")


    def report_first_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_second_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_third_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]


    message = models.IntegerField(label="")

    def message_choices(self):
        return [[1, 'Up'], [2, 'Middle'], [3, 'Down']]

    guess = models.IntegerField(label="")

    def guess_choices(self):
        return[[1, 'Up'], [2, 'Middle'], [3, 'Down']]

    check_first = models.IntegerField(label="")

    check_second = models.IntegerField(label="")

    check_third = models.IntegerField(label="")


    def get_state(self):
        self.true_state = random.choices([1, 2, 3], weights = [Constants.initial_prior, Constants.initial_prior, Constants.initial_prior])[0]
        print(self.true_state)
        return self.true_state


    def get_correct_attributes(self):
        if self.message == 1:
            self.attribute_first =  self.session.vars['Simple_Up'][self.round_number - 1][0]
            self.attribute_second =  self.session.vars['Simple_Up'][self.round_number - 1][1]
            self.attribute_third =  self.session.vars['Simple_Up'][self.round_number - 1][2]
        elif self.message == 2:
            self.attribute_first = self.session.vars['Simple_Middle'][self.round_number - 1][0]
            self.attribute_second = self.session.vars['Simple_Middle'][self.round_number - 1][1]
            self.attribute_third = self.session.vars['Simple_Middle'][self.round_number - 1][2]
        else:
            self.attribute_first =  self.session.vars['Simple_Down'][self.round_number - 1][0]
            self.attribute_second =  self.session.vars['Simple_Down'][self.round_number - 1][1]
            self.attribute_third =  self.session.vars['Simple_Down'][self.round_number - 1][2]
        print(self.attribute_first)
        print(self.attribute_second)
        print(self.attribute_third)
        return self.attribute_first, self.attribute_second, self.attribute_third



    def get_check_first(self):
        if self.attribute_first == self.report_first:
            self.check_first = 1
        else:
            self.check_first = 0

        # print(self.attribute_first)
        # print(self.report_first)
        # print(self.check_first)
        # return self.check_first


    def get_check_second(self):
        if self.attribute_second == self.report_second:
            self.check_second = 1
        else:
            self.check_second = 0

        # print(self.attribute_second)
        # print(self.report_second)
        # print(self.check_second)
        # print(self.check_second)
        # return self.check_second


    def get_check_third(self):
        if self.attribute_third == self.report_third:
            self.check_third = 1
        else:
            self.check_third = 0

        # print(self.attribute_third)
        # print(self.report_third)
        # print(self.check_third)
        # print(self.check_third)
        # return self.check_third
        #



#when the final set is decided, add a function to examine whether the sender is truthfully reporting.

class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    other_payoff = models.CurrencyField()


    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'




