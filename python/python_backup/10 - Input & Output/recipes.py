import shelve

# blt = ['bacon', 'lettuce', 'tomato']
# beans_on_toast = ['beans', 'bread']
# scrambled_eggs = [ 'eggs', 'butter', 'milk']
soup = ['tin of soup']
# pasta = ['pasta', 'cheese']

with shelve.open('recipies') as recipies:
    # recipies['blt'] = blt
    # recipies['beans on toast'] = beans_on_toast
    # recipies['scrambled_eggs'] = scrambled_eggs
    # recipies['soup'] = soup
    # recipies['pasta'] = pasta

    for snack in recipies:
        print(snack, recipies[snack])

    temp_list = recipies['blt']
    temp_list.append('butter')
    print(temp_list)
    recipies['blt'] = temp_list

    temp_list = recipies['pasta']
    temp_list.append('tomato')
    print(temp_list)
    recipies['pasta'] = temp_list
    

    recipies['soup'] = soup
    recipies.sync() # this method clears the cache
    soup.append('cream')

    for snack in recipies:
        print(snack, recipies[snack])