cats = {
    'suki':{
        'name':'Suki',
        'age':13
    },
    'fizz':{
        'name':'Fizz',
        'age':14
    }
}

for k,cat in cats.items():
    sentence = 'My cat %s is %i years old.' % (cat['name'], cat['age'])

    print(sentence)