#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
gato1 = Cat('michi',10000)
gato2 = Cat('pixi',1300)
gato3 = Cat('batu',92999)

# 2 Create a function that finds the oldest cat
cats_list = [gato1,gato2, gato3]

def older_cat(cats):
    oldest = 0 
    print('\nIs time to know how is the oldest cat:')
    for i in range(len(cats)):
        if cats[oldest].age < cats[i].age: 
            oldest = i
            print(f'there are a new older cat: {cats[oldest].name}')
        else: 
            print(f'currently {cats[oldest].name} is the oldest cat')
    print(f'\n\tFinally the oldest cat is {cats[oldest].name} with {cats[oldest].name} years old')


older_cat(cats_list)


#Solution using list methods
def oldest(*args):
    ages = []
    for object in args:
        ages.append(object.age)
    return max(ages)

print(f'\n\nThe oldest cat is {oldest(gato1,gato2, gato3)} years old.')