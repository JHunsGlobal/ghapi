# AUTOGENERATED! DO NOT EDIT! File to edit: 04_event.ipynb (unless otherwise specified).

__all__ = ['fetch_events']

# Cell
from fastcore.utils import *
from fastcore.foundation import *
from .core import *

import time

# Cell
def fetch_events(types=None):
    "Generate an infinite stream of events optionally filtered to `types`"
    if types: types=setify(types)
    seen = set()
    while True:
        evts = [o for o in api.activity.list_public_events() if o.id not in seen]
        print('***', len(evts))
        for o in evts:
            seen.add(o.id)
            if not types or o.type in types: yield o
        time.sleep(0.5)