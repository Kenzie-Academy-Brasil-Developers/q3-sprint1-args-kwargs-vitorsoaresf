import functools
def sum_numbers(*args):
    return functools.reduce(lambda a,b: a+b, args)

# numbers = [1, 2, 3, 4, 5, 6]
# print(sum_numbers(*numbers))

def get_multiplied_amount(multiplier, *args):
    return multiplier * functools.reduce(lambda a,b: a+b, args)

# numbers = [1, 2, 3]
# multiplier = 2
# print(get_multiplied_amount(multiplier, *numbers))

def word_concatenator(*args):
    return " ".join(args)

# words = ["Tá", "pegando", "fogo", "bicho!!!", " "]
# print(word_concatenator(*words))

def inverted_word_factory(*args):
    result = [x[::-1] for x in args]
    result.reverse()
    return " ".join(result)

# words = ["eae", "amigão", "belezinha?"]
# print(inverted_word_factory(*words))

def dictionary_separator(**kwargs):    
    return (list(kwargs.keys()),list(kwargs.values()))

# user = {
#     "name": "Naruto",
#     "age": 16,
#     "favorite word": "Ichiraku Ramen"
# }
# print(dictionary_separator(**user)) 

def dictionary_creator(*args, **kwargs):
    result = {}
    if(len(args) < len(kwargs)):
        return None
    
    for element in zip(args,kwargs.values()):
        result[element[0]] = element[1]
    
    return result

# change_keys = ["username", "password", "address"]
# user = {
#     "name": "Williams",
#     "key": "1234"
# }

# print(dictionary_creator(*change_keys,**user))

def purchase_logger(**kwargs):
    return f"Product {kwargs['name']} costs {kwargs['price']} and was bought {kwargs['quantity']}"

# purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}
# print(purchase_logger(**purchase))

# def world_cup_logger(country, *args):
#     return f"{country} - {sorted(args)}"

# country = 'Alemanha'
# year_list = [2014, 1990, 1974, 1954]

# print(world_cup_logger(country, *year_list))
