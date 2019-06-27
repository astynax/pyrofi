### About

PyRofi wraps [Rofi](https://github.com/davatorium/rofi) and helps you to build the hierarchical menus with neat navigation.

### Installation

Just `python3 -m pip install --update --user pyrofi` (requires Python `^3.6`).

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

More complex example you can see [here](https://github.com/astynax/pyrofi/blob/master/pyrofi/__main__.py) and run it with `python3 -m pyrofi`.
