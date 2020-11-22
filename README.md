### About

![PyPI - License](https://img.shields.io/pypi/l/pyrofi.svg)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyrofi.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrofi.svg)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/astynax/pyrofi.svg)
[![PyPI](https://img.shields.io/pypi/v/pyrofi.svg)](https://pypi.org/project/pyrofi/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

PyRofi wraps [Rofi](https://github.com/davatorium/rofi) and helps you to build the hierarchical menus with neat navigation. You can also use [Wofi](https://hg.sr.ht/~scoopta/wofi) as the "backend".

### Installation

Make sure that you have Rofi or the Wofi installed. Then just `python3 -m pip install --update --user pyrofi` (requires Python `^3.6`).

### Menu structure

Every menu is just a dictionary: the keys are menu item captions, values are **actions** or **submenus**.

```python
run_menu({
    'command': ['man', 'ls'],
    'submenu': {
        'command': [...],
        ...
    },
})
```

Submenus are just dictionaries with the same structure.

Action can be:

- the "command" — a list with command plus arguments
    ```python
    'google': ['firefox', 'https://google.com']`
    ```
- some `Callable[List[str], ]` that receives a path to the item and returns
    - `None` if all the work is done and you need to stop the interaction
    - a command (see above)
        ```python
        def show_path(path):
            return ['echo'] + path

        ...
        'where am I': show_path
        ```
    - a submenu to "dive" into (you can build the submenus dynamically)
        ```python
        def games_menu(path):
            return {
                ...
            }

        'games': games_menu
        ```

Also, the `run_menu` function can receive a `callback: Callable[List[Any], bool]` argument: that's how you can override the command execution. Any callback function should take a path as a sole argument and return either `True` if no more interactions are needed or `False` if you want to keep the menu active.

### Example

```python
#!/usr/bin/env python3

from pyrofi import run_menu

def hello_world(_):
    print('Hello World!')

def dice():
    import random
    return ['echo', random.choice('123456')]

run_menu({
    'Calculator': ['xcalc'],
    'Games': {
        'Rogue': ['rogue'],
        'Angband': ['angband']
    },
    'Calendar': ['ncal', '2019'],
    'Hello World': hello_world,
    'Dice': dice,
})
```

If you want to use Wofi, you will need to add `menu_cmd=pyrofi.WOFI_CMD` (or just `menu_cmd='wofi`) to the `run_menu` call.

More complex example you can see [here](https://github.com/astynax/pyrofi/blob/master/pyrofi/__main__.py) and run it with `python3 -m pyrofi`.
