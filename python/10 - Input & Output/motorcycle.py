import shelve

with shelve.open('bike') as bike:
    bike['bike'] = 'Honda'
    bike['model'] = '250 Dream'
    bike['colour'] = 'red'
    bike['engine_size'] = 250
    for key in bike:
        print(key)
    
    # del bike['mike'] - This is how you delete an object from the shelf
    
    print('=' * 40)


    print(bike['engine_size'])
    print(bike['colour'])