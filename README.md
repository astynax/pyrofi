### About

PyRofi wraps [Rofi](https://github.com/davatorium/rofi) and helps you to build the hierarchical menus with neat navigation.

### Installation

Just `python3 -m pip install --user pyrofi`.

### Example

```python
#!/usr/bin/env python3

from pyrofi import run

run({
    'Calculator': ['xcalc'],
    'Games': {
        'Rogue': ['rogue'],
        'Angband': ['angband']
    },
    'Calendar': ['ncal', '2019']
})
```

(You can run a similar example with `python -m pyrofi.menu`).
