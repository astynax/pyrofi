# -*- coding: utf-8 -*-

"""Rofi Menu wrapper for hierarchical menu creation."""

from os import execlp
from subprocess import PIPE, Popen  # noqa: S404
from typing import Any, Callable, List

__all__ = ('QUICK', 'run_menu', 'execute')


# Reasonable set of flags: auto-selecting, no history & case sensitivity.
QUICK = (
    '-i',
    '-auto-select',
    '-disable-history',
    '-no-custom',
)


def execute(args: List[str]) -> bool:
    """Just execute @args as external command."""
    execlp(args[0], ' ', *args[1:])  # noqa: S606
    return True


def make_rofi_cmd(
    *args: str,
    prefix='',
    **kwargs: str,
):
    cmd_line = (
        'rofi',
    ) + tuple(args) + tuple(
        i
        for k, v in kwargs.items()
        for i in ('-' + k, v)
    ) + ('-dmenu', '-p')
    return lambda path: cmd_line + (
        prefix + '/'.join(path or ()) + ' :',
    )


def run_dmenu(
    path_to_cmd: Callable[[List[str]], List[str]],
    menu_items: List[str],
    path: List[str],
):
    proc = Popen(path_to_cmd(path), stdin=PIPE, stdout=PIPE)  # noqa: S603
    out, _ = proc.communicate(
        bytes('\n'.join(sorted(menu_items)), 'utf-8'),
    )
    ret_code = proc.poll()
    return (not ret_code and out.decode('utf-8')) or None


def run_menu(  # noqa: Z210, Z212
    menu: dict,
    *args: str,
    prefix='',
    callback: Callable[[Any], bool] = execute,
    **kwargs: str,
):
    """Run the @menu with optional @config."""
    make_cmd = make_rofi_cmd(*args, prefix=prefix, **kwargs)

    def walk(menu, path):  # noqa: Z430
        while True:
            key = run_dmenu(
                make_cmd,
                (path and ['..'] or []) + [
                    k + ('/' if isinstance(v, dict) else '')
                    for k, v in menu.items()
                ],
                path,
            )
            if key is None:
                return False
            key = key.strip().rstrip('/')
            if key == '..':
                # go up and continue
                return True
            try:
                menu_item = menu[key]
            except KeyError:
                return False
            while True:
                if isinstance(menu_item, dict):
                    # item is a sub-menu, walk through it
                    if walk(menu_item, path + (key,)):
                        # back to menu
                        break
                elif callable(menu_item):
                    # item is callable, call it
                    menu_item = menu_item(path)
                    if menu_item is not None:
                        # a continuation was returned, use it
                        continue
                else:
                    # item is a regular cmd, run it and exit
                    call_result = callback(menu_item)
                    if call_result:
                        # back to menu
                        break
                # all done, exit then
                return False

    walk(menu, ())
