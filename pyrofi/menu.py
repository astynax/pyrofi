# -*- coding: utf-8 -*-

"""Pyrofi menu builder."""


from os import execlp
from subprocess import PIPE, Popen  # noqa: S404

__all__ = ('QUICK', 'run')


# Reasonable set of flags: auto-selecting, no history & case sensitivity.
QUICK = (
    '-i',
    '-auto-select',
    '-disable-history',
    '-no-custom',
)


def make_cmd(*args, prefix=None, **kwargs):
    cmd_line = (
        'rofi',
    ) + tuple(args) + tuple(
        i
        for k, v in kwargs.items()
        for i in ('-' + k, v)
    )
    return lambda path: cmd_line + (
        '-p',
        (prefix or '') + '/'.join(path or ()) + ' :',
        '-dmenu',
    )


def run_dmenu(cmd, menu_items, path=None):
    proc = Popen(cmd(path), stdin=PIPE, stdout=PIPE)  # noqa: S603
    out, _ = proc.communicate(
        bytes('\n'.join(sorted(menu_items)), 'utf-8'),
    )
    ret_code = proc.poll()
    return (not ret_code and out.decode('utf-8')) or None


def run(menu, *args, **kwargs):
    """Run the @menu with optional @config."""
    cmd = make_cmd(*args, **kwargs)

    def walk(menu, path=None):
        while True:
            key = run_dmenu(
                cmd,
                (path and ['..'] or []) + [
                    k + ('/' if isinstance(v, dict) else '')
                    for k, v in menu.items()
                ],
                path,
            )
            if key is not None:
                key = key.strip().rstrip('/')
                if key == '..':
                    return False
                try:
                    menu_item = menu[key]
                except KeyError:
                    return True
                if isinstance(menu_item, dict):
                    if walk(menu_item, (path or ()) + (key,)):
                        break  # noqa: Z220
                else:
                    execlp(menu_item[0], ' ', *menu_item[1:])  # noqa: S606
                    break
            else:
                break
        return True

    return walk(menu)


if __name__ == '__main__':
    run({
        'Games': {
            'RPG': {
                'Angband': ['echo', 'angband'],
                'Rogue': ['echo', 'rogue'],
            },
            'Arcade': {
                'Frogger': ['echo', 'frogger'],
            },
        }, 'Tools': {
            'Calendar': ['cal'],
            'System Name': ['uname'],
        },
    },
        *QUICK,
        '-fixed-num-lines',
        prefix='MENU ',
        lines='3',
        width='-20',
        location='0',
    )
