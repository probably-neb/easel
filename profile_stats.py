import pstats
from pstats import SortKey

p = pstats.Stats('profile.txt')
# p.strip_dirs().sort_stats(-1).print_stats()
# p.sort_stats(SortKey.NAME)
# p.print_stats()
# p.sort_stats(SortKey.TIME).print_stats(25)
# p.sort_stats(SortKey.TIME).print_stats(10)
# p.sort_stats(SortKey.FILENAME).print_stats('__init__')
p.sort_stats(SortKey.TIME).print_callers(.25).reverse_order().print_stats()
