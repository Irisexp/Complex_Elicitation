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
Memory test
"""


class Constants(BaseConstants):
    name_in_url = 'MemoryCards'
    players_per_group = None
    time = 15
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    average = models.FloatField()

    def set_payoffs(self):
        players = self.get_players()
        correct = [p.correct for p in players]
        print(correct)
        self.average = round(sum(correct)/len(players),1)
        print('group average)')
        print(self.average)


class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    report_first = models.IntegerField(label="")

    report_second = models.IntegerField(label="")

    report_third = models.IntegerField(label="")

    report_fourth = models.IntegerField(label="")

    report_fifth = models.IntegerField(label="")

    report_sixth = models.IntegerField(label="")

    report_seventh = models.IntegerField(label="")

    report_eighth = models.IntegerField(label="")

    report_ninth = models.IntegerField(label="")

    report_tenth = models.IntegerField(label="")

    report_eleventh = models.IntegerField(label="")

    report_twelfth = models.IntegerField(label="")

    report_thirteenth = models.IntegerField(label="")

    report_fourteenth = models.IntegerField(label="")

    report_fifteenth = models.IntegerField(label="")

    report_sixteenth = models.IntegerField(label="")

    report_seventeenth = models.IntegerField(label="")

    report_eighteenth = models.IntegerField(label="")

    report_nineteenth = models.IntegerField(label="")

    report_twentieth = models.IntegerField(label="")

    check_first = models.IntegerField(label="")

    check_second = models.IntegerField(label="")

    check_third = models.IntegerField(label="")

    check_fourth = models.IntegerField(label="")

    check_fifth = models.IntegerField(label="")

    check_sixth = models.IntegerField(label="")

    check_seventh = models.IntegerField(label="")

    check_eighth = models.IntegerField(label="")

    check_ninth = models.IntegerField(label="")

    check_tenth = models.IntegerField(label="")

    check_eleventh = models.IntegerField(label="")

    check_twelfth = models.IntegerField(label="")

    check_thirteenth = models.IntegerField(label="")

    check_fourteenth = models.IntegerField(label="")

    check_fifteenth = models.IntegerField(label="")

    check_sixteenth = models.IntegerField(label="")

    check_seventeenth = models.IntegerField(label="")

    check_eighteenth = models.IntegerField(label="")

    check_nineteenth = models.IntegerField(label="")

    check_twentieth = models.IntegerField(label="")

    correct = models.IntegerField(label="")

    guess_yours = models.FloatField(lable="", choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    guess_average = models.FloatField(label="", choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


    def report_first_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_second_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_third_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                [11, 'H'], [12, 'P']]

    def report_fourth_choices(self):
        return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                [10, '7'], [11, '12'], [12, '16']]

    def report_fifth_choices(self):
        return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'], [7, '\u221A'],
                [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def report_sixth_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_seventh_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_eighth_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                [11, 'H'], [12, 'P']]

    def report_ninth_choices(self):
        return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                [10, '7'], [11, '12'], [12, '16']]

    def report_tenth_choices(self):
        return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'], [7, '\u221A'],
                [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def report_eleventh_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_twelfth_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_thirteenth_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                [11, 'H'], [12, 'P']]

    def report_fourteenth_choices(self):
        return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                [10, '7'], [11, '12'], [12, '16']]

    def report_fifteenth_choices(self):
        return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'], [7, '\u221A'],
                [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def report_sixteenth_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_seventeenth_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_eighteenth_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                [11, 'H'], [12, 'P']]

    def report_nineteenth_choices(self):
        return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                [10, '7'], [11, '12'], [12, '16']]

    def report_twentieth_choices(self):
        return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'], [7, '\u221A'],
                [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def get_check_first(self):
        print(self.report_first)
        if self.report_first == 3:
            self.check_first = 1
        else:
            self.check_first = 0
        print(self.check_first)

    def get_check_second(self):
        print(self.report_second)
        if self.report_second == 1:
            self.check_second = 1
        else:
            self.check_second = 0

    def get_check_third(self):
        if self.report_third == 10:
            self.check_third = 1
        else:
            self.check_third = 0

    def get_check_fourth(self):
        if self.report_fourth == 1:
            self.check_fourth = 1
        else:
            self.check_fourth = 0

    def get_check_fifth(self):
        if self.report_fifth == 1:
            self.check_fifth = 1
        else:
            self.check_fifth = 0

    def get_check_sixth(self):
        if self.report_sixth == 2:
            self.check_sixth = 1
        else:
            self.check_sixth = 0

    def get_check_seventh(self):
        if self.report_seventh == 3:
            self.check_seventh = 1
        else:
            self.check_seventh = 0

    def get_check_eighth(self):
        if self.report_eighth == 1:
            self.check_eighth = 1
        else:
            self.check_eighth = 0

    def get_check_ninth(self):
        if self.report_ninth == 8:
            self.check_ninth = 1
        else:
            self.check_ninth = 0

    def get_check_tenth(self):
        if self.report_tenth == 3:
            self.check_tenth = 1
        else:
            self.check_tenth = 0

    def get_check_eleventh(self):
        if self.report_eleventh == 9:
            self.check_eleventh = 1
        else:
            self.check_eleventh = 0

    def get_check_twelfth(self):
        if self.report_twelfth == 8:
            self.check_twelfth = 1
        else:
            self.check_twelfth = 0

    def get_check_thirteenth(self):
        if self.report_thirteenth == 11:
            self.check_thirteenth = 1
        else:
            self.check_thirteenth = 0

    def get_check_fourteenth(self):
        if self.report_fourteenth == 9:
            self.check_fourteenth = 1
        else:
            self.check_fourteenth = 0

    def get_check_fifteenth(self):
        if self.report_fifteenth == 7:
            self.check_fifteenth = 1
        else:
            self.check_fifteenth = 0

    def get_check_sixteenth(self):
        if self.report_sixteenth == 6:
            self.check_sixteenth = 1
        else:
            self.check_sixteenth = 0

    def get_check_seventeenth(self):
        if self.report_seventeenth == 4:
            self.check_seventeenth = 1
        else:
            self.check_seventeenth = 0

    def get_check_eighteenth(self):
        if self.report_eighteenth == 7:
            self.check_eighteenth = 1
        else:
            self.check_eighteenth = 0

    def get_check_nineteenth(self):
        if self.report_nineteenth == 12:
            self.check_nineteenth = 1
        else:
            self.check_nineteenth = 0

    def get_check_twentieth(self):
        if self.report_twentieth == 4:
            self.check_twentieth = 1
        else:
            self.check_twentieth = 0

    def get_correct(self):
        self.correct = self.check_first + self.check_second + self.check_third + self.check_fourth + self.check_fifth + self.check_sixth + self.check_seventh + self.check_eighth + self.check_ninth + \
                       self.check_tenth + self.check_eleventh + self.check_twelfth + self.check_thirteenth + self.check_fourteenth + self.check_fifteenth + self.check_sixteenth + self.check_seventeenth + self.check_eighteenth + self.check_nineteenth + self.check_twentieth



