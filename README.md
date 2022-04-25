```
from tinystore.models import TinyStore

TinyStore.get('omg') # {'test': 42}
TinyStore.exists('omg') # False
TinyStore.keys() # []

TinyStore.set('omg', {'a': 1})

TinyStore.get('omg') # {'a': 1}
TinyStore.exists('omg') # True
TinyStore.keys() # ['omg']
```

Set defaults in `settings.py`
