# a
# scores = {'Amanda': [88, 92, 100], 'Kennet': [30, 45, 50], 'Einstein': [100,100,100]}
# 88,92,100
# 100

# b


frukt = {
    'Banan': '1',  # dict
    'Eple': '2',
    'Mango': '3',
}
print(frukt)

# c
frukt.update({'Kiwi': '0', 'Umoden Banan': '0'})  # update


if 'Banan' and 'Eple' and 'Mango' in frukt:  # cond.
    del frukt['Banan']  # del
    del frukt['Eple']
    del frukt['Mango']
    print(frukt)  # print

# d

for key, value in frukt.items():  # for (key) og (value) i frukt
    print(value)  # printer value

# e
if 'bananer' in frukt:  # sjekker for bananer
    del frukt['bananer']  # sletter bananer
else:
    print(frukt)

# f

frukt.update({'Jordbar': '10', 'Blaabar': '20'})  # update frukt med jordbær og blåbær
for key, value in frukt.items():  # itererer key, value i frukt
    print(key, value)  # printer ut begge
