#goal here is to remove extra spaces and the resulting null values produced from str.split(' ')
def cleaner(input) -> str: #insert ['list', 'of', 'strings', 'to remove "" and " "']
    x = 0
    while x < 100:
        try:
            input.remove('')
            x = x + 1
        except:
            x = 10000
    x = 0
    while x < 100:
        try:
            input.remove(' ')
            x = x + 1
        except:
            x = 10000
    return(input)
