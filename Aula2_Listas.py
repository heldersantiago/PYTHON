# This Lesson will talk about the LIST at Python

Prg_Lg = ['python','javaScript','C#','C++']

print(' \n\nWhat video Language above Would you like to Seek at BD? \n\t')
print(Prg_Lg)
print('\nIt is all i could find,Sir! ')
print('\tIs there missing some?')
ans = input("\tYes or NOt\n\t").lower()
keep = ''

while keep != 'not':

    if ans == 'yes':
        print(" Would you like to Add a language? ")
        _as = input("Yes or NOt\n\t").lower()
        if _as == 'yes':
            lg = input("Digite o nome da Linguagem\n\t")
            Prg_Lg.append(lg) 
        elif _as == 'not':
            print('No language was Add to the Base Data ')
    elif ans == 'not':
        print('Thanks for Coming')
        
    print(" There is the list", Prg_Lg)
    keep = input(" \n\n\tWOULD YOU LIKE TO KEEP ON? Yes or NOt? ").lower()