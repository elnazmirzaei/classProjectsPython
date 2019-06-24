#timeit_example.py
import timeit

# using setitem
t = timeit.Timer("cd = [];",
"for i in range(0,m):",
"	cd.append(0);")

print('TIMEIT:')
print(t.timeit(5))

print('REPEAT:')
print(t.repeat(3, 3))