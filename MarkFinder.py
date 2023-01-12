import Search_Parse

def Mark_Test(stringIn, substringIn):
    Mark = []
    try:        
        index = Search_Parse.Search(stringIn, substringIn)
        Mark.append(stringIn[index])
    except:
        pass
    try:
        if Mark[0] != '':
            status = True
            return(status, Mark)
    except:
        status = False
        return(status, Mark) #returns if success or fail, and the mark found.

