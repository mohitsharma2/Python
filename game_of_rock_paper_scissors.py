while(True):
    inp=input('Enter only choice among rock,paper or scissors')
    import random
    from random import randint
    a=random.choice(['rock','paper','scissors'])
    print(a)
    if inp in ['rock','paper','scissors']:
        if inp==a:
            print('wins')
        elif inp!=a:
            print('lost')
    else:
        print('invalid input')
      
        







