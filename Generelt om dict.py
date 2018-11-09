# a)
# b)
# c


my_family = {}  # tom dict


def add_family_member(role, name):
    my_family[role] = name  # role = name


add_family_member('Onkel', 'Bjørn')  # legger til familiemedlem
print(my_family)

add_family_member('Pappa', 'Anders')  # legger til familiemedlem
print(my_family)


onkel = ['Vemund']  # definerer et familiemedlem


add_family_member('Onkel', onkel)  # legger til enda et familiemedlem
print(my_family)
