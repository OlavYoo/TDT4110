# a
my_set = set()  # tomt set

# b

for x in range(0, 21):
    if x % 2 != 0:
        my_set.add(x)
print(my_set)

# c

my_set2 = set()
for x in range(0, 11):
    if x % 2 != 0:
        my_set2.add(x)
print(my_set2)

# d

my_set3 = my_set.difference(my_set2)
my_set3 = my_set-my_set2
print(my_set3)


# e
# ingenting, set()

# f


def allunique(lst):

    list_set = set(lst)  # konverterer til set, set kan kun være unike
    if len(lst) == len(list_set):  # if løkke som sjekker lengden og returnerer
        return True  # True eller
    else:
        return False  # False


print(allunique([1, 2, 3, ]))  # Listen


# g


def removeDuplicates(lst):

    uten_duplikat = set(lst)  # set uten duplikater
    ny_liste = set(uten_duplikat)  # nytt sett
    return ny_liste  # returnerer nytt sett


print(removeDuplicates([1, 2, 3, 3, 5, 6, 7, 7]))  # Originallisten
