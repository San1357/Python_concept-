'''Problem : Print multiplication table of 14 from a list in which multiplication table of 12 is stored.'''






#CODE:

table_12 = []
for i in range(1,121):
    if i % 12 == 0:
        table_12.append(i)
print(table_12)

table_14 = []
for i, j in enumerate(table_12):
    table_14.append(j+(i+1)*2)
print(table_14)
