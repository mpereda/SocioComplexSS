from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number == 1:
            yield (views.Welcome)

        yield (views.Decision, {'decision': random.choice(['A','B'])})
        yield (views.Results)

