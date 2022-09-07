```
from tinystore.models import TinyStore

TinyStore.get('omg')  # None
TinyStore.exists('omg')  # False
TinyStore.keys()  # []

TinyStore.set('omg', {'a': 1})
TinyStore.get('omg')  # {'a': 1}
TinyStore.exists('omg')  # True
TinyStore.keys()  # ['omg']

TinyStore.remove('omg')
TinyStore.keys()  # []
# or
TinyStore.remove_all()
TinyStore.keys()  # []
```

Optionally, set defaults in `settings.py`, e.g.

```
TINY_STORE = {
    'omg: {'test': 42},
    'lol: {'key': 'value'},
}
```
