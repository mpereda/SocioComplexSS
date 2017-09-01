from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Welcome(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']

    timeout_seconds = 30

    def vars_for_template(self):

        history_of_player = self.player.in_previous_rounds() if self.round_number < (1 + Constants.memory_size) else self.player.in_rounds(self.round_number-4, self.round_number-1)

        return {
            'player_in_previous_rounds': history_of_player,
        }

    def before_next_page(self):
        if self.timeout_happened:
            self.player.decision = random.choice(['A','B'])


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_minority()
        self.group.set_payoffs()


class Results(Page):
    timeout_seconds = 20

    def vars_for_template(self):

        history_of_player = self.player.in_all_rounds() if self.round_number < Constants.memory_size else self.player.in_rounds(self.round_number-3, self.round_number)

        return {
            'player_in_previous_rounds': history_of_player,
        }


class LastResults(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


page_sequence = [
    Welcome,
    Decision,
    ResultsWaitPage,
    Results,
    LastResults
]
