#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза'}
meadow_set ={'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка'}
all_flowers = garden_set.union(meadow_set)

# выведите на консоль все виды цветов

print('Все цветы', all_flowers)

# выведите на консоль те, которые растут и там и там
general = garden_set & meadow_set
print('Цветы растущие и в саду, и на лугу:', general)

# выведите на консоль те, которые растут в саду, но не растут на лугу
diff_set = garden_set.difference(meadow_set)
print('Цветы растущие в сдау, но не растущие на лугу:', diff_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
diff_set_2 = meadow_set.difference(garden_set)
print('Цветы растущие на лугу, но не растут в саду:', diff_set_2)


