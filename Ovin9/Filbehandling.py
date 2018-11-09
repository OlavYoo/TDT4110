# a


def write_to_file(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close()


write_to_file('Hei')

# b


def read_from_filename(filename):
    f = open(filename, 'r')
    innhold = f.read()
    print(innhold)
    f.close()


read_from_filename('filename.txt')


# c


def main():
    evig = 0  # kontrollerer løkken
    while evig == 0:  # while løkke
        svar = str(input("Do you want to read or write? "))  # spør brukeren om hva som er ønsket
        if svar.lower() == 'write':
            data = str(input("What do you want to write? "))
            write_to_file(data)  # kaller på write
        if svar.lower() == 'read':
            read_from_filename('filename.txt')  # kaller på read
        if svar.lower() == 'done':
            print("You are done")
            return  # avslutter hvis svar = done


main()
