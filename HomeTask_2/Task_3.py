# Write a script to remove an empty tuple(s) from a list of tuples.

tup_list = [(), (), ('name', 'age'), ('Hello', 'Car'), (), ('',)]
tup_list = [n for n in tup_list if n]
print(tup_list)