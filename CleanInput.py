#goal here is to remove extra spaces and the resulting null values produced from str.split(' ')
def cleaner(input) -> list: #insert ['list', 'of', 'strings', 'to remove "" and " "']
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

def cleanString(strIn) -> str:
    w = strIn.split(' ')
    w = cleaner(w)
    w = (" ").join(w)
    return(w)

#print(cleanString("this     is a test of a      string i     want cleaned"))

