### About

![PyPI - License](https://img.shields.io/pypi/l/pyrofi.svg)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyrofi.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrofi.svg)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/astynax/pyrofi.svg)
[![PyPI](https://img.shields.io/pypi/v/pyrofi.svg)](https://pypi.org/project/pyrofi/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

PyRofi wraps [Rofi](https://github.com/davatorium/rofi) and helps you to build the hierarchical menus with neat navigation. You can also use te [Wofi](https://hg.sr.ht/~scoopta/wofi) as the "backend".

### Installation

Make sure that you have the Rofi or the Wofi installed. Then just `python3 -m pip install --update --user pyrofi` (requires Python `^3.6`).

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
