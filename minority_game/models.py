from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'minority_game'
    players_per_group = 2
    num_rounds = 6
    memory_size = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    minority=models.CharField()

    def set_minority(self):
        sum_A = sum(1 if p.decision=="A" else 0 for p in self.get_players())
        sum_B = sum(1 if p.decision == "B" else 0 for p in self.get_players())

        if sum_A == sum_B:
            self.minority="both"

        else:
            if sum_A < sum_B:
                self.minority="A"
            else:
                self.minority="B"

    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = 1 if (p.decision == p.group.minority or p.group.minority=="both") else 0


class Player(BasePlayer):
    choices = ("A", "B")
    decision = models.CharField(initial=None, widget=widgets.RadioSelectHorizontal(),
                                        verbose_name='Make your choice',
                                        choices=choices)
