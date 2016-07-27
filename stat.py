import pstats
p = pstats.Stats("output.txt")
p.strip_dirs().sort_stats(1).print_stats()