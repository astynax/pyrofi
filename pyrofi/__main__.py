# -*- coding: utf-8 -*-

"""Pyrofi demonstration."""

from pyrofi import QUICK, execute, run_menu

if __name__ == '__main__':

    def roll_dice(_):
        import random
        return random.choice('123456')  # this will be an arg for callback

    def go_deeper(_):
        return {
            'And deeper': go_deeper,
            'Stop': print,  # this will print the path
        }

    run_menu({
        'Games': {
            'RPG': {
                'Angband': 'angband',
                'Rogue': 'rogue',
            },
            'Arcade': {
                'Frogger': 'frogger',
            },
        }, 'Tools': {
            'Calendar': 'cal',
            'System Name': 'uname',
        },
        'Hello World': (lambda _: print('Hello world!')),
        'Dice': roll_dice,
        'Go deep': go_deeper,
    },
        *QUICK,
        '-fixed-num-lines',
        callback=(
            # execute "echo" for every "simple" item
            lambda arg: execute(['echo', arg]) and False
        ),
        prefix='MENU ',
        lines='5',
        width='-40',
        location='0',
    )
