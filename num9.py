order = {'15':'lemon soda','20':'water','16':'coke'}

select = input("Input money : ")

if(order[select] == 'lemon soda'):
    print('lemon soda')
elif order[select] == 'water':
    print('water')
elif order[select] == 'coke':
    print('coke')