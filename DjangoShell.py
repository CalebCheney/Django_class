import os
from re import T
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

for t in topics:
    print(t.id, ' ', t) #or t.text to get only text if added other info

t = Topic.objects.get(id = 1) #following returns only for  chess bc it has id 1

print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for e in entries:
    print(e) #e.text bypasses the str method stating to only return 50 characters. (returns whole string message)

