 # a

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n+recursive_sum(n-1)


print(recursive_sum(53))


 # b )

def fakultet(n):
    if n<2:
        return 1
    else:
        return n*fakultet(n-1)
print(fakultet(5))

# c


def find_smallest_element(l):
    if len(l) == 0:
        raise ValueError('Tom liste!')  # tom liste gir vr
    elif len(l) == 1:  # lengde på listen 1
        return l[0]
    else:
        minNum = find_smallest_element(l[1:])  # rekursivt kall etter 1:
        min = l[0]  # setter minimum til index 0 i listen
        if minNum < min:  # dersom minNum < min
            min = minNum  # min = minNum (skjer v rekursjon)
        return min  # returner min

print(find_smallest_element([3,2,1,2,-4,3,4,4]))


"""def binary_search(numbers, element):
    first = 0
    last = numbers

    if len(numbers) == 0:
        raise ValueError('Tom liste!!')
    else:
        søk = (first + last // '2')
        if element == numbers [søk]:
            return 'Jippikaye maddafakka'
        else:
            if numbers[søk] < element:
                return binary_search(numbers[søk+1], element)
            else:
                return binary_search(numbers[:søk], element)
print(binary_search([1,2,3,4,5], 5))"""

def binary_search(numbers,element):
    i = len(numbers)//2  # splitter listen i to
    if element > numbers[i]:  # sjekker etter element
       søk = binarySearch(numbers[i+1:],element)  # søker etter element v. split og i+1
       if søk:
          return binarySearch(numbers[i+1],element)+c+1  # dersom elementet er funnet
    elif element < numbers[i]:  # hvis element < søket
       return binarySearch(numbers[:i],element)  # prøver igjen ved split
    else:
       return i

print(binary_search([1,5,8,10,20,50,60],10))



