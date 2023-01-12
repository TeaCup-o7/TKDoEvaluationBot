
import True_Harm
import Pure_Water_Remain

def evalAlliances(Sub, Gre, Les):
    score = 0
    if len(Sub) == 1:
        score = score + 4
    elif len(Gre) == 3: #accounts for only GA complete if only when no sublime(ELIF)
        score = score + 3
    elif (len(Gre) + len(Les)) == 6: #this accounts for if did all LA and 1 or 2 GA
        score = score + 2
    elif len(Les) == 6: #accounts for complete 6 LA or no GA
        score = score + 2
    elif len(Les) >= 3: #accounts for complete only 3 LA
        score = score + 1
    else:
        print("not enough alliances or something went wrong.")
    return(score)

def evalHajio(test):
    Total, Hscore, mark, marks = Pure_Water_Remain.Hanjiho(test)
    score = 0
    if (Total >= 5):
        score = score + 1
    if (Total >= 10):
        score = score + 1
    if (Total >= 25):
        score = score + 1
    if (Total >= 50):
        score = score + 1
    return(score, marks)

def True_Harm_Final(test):
    Total , marks = Pure_Water_Remain.Hanjiho(test)
    print('STARTING TRUE HARM FINAL')
    Sublime, Greaters, Lessers = True_Harm.alliance(test)
    Hanjiho_counter = Total
    Endstudied = True_Harm.Studiedtest(test)
    SLen = len(Sublime)
    GLen = len(Greaters)
    LLen = len(Lessers)
    THC = 0
    print(SLen)
    print(GLen)
    print(LLen)


    if SLen == 1:
        THC = THC + 4
    elif GLen == 3: #accounts for only GA complete if only when no sublime(ELIF)
        THC = THC + 3
    elif GLen + LLen == 6: #this accounts for if did all LA and 1 or 2 GA
        THC = THC + 2
    elif LLen == 6: #accounts for complete 6 LA or no GA
        THC = THC + 2
    elif LLen >= 3: #accounts for complete only 3 LA
        THC = THC + 1
    else:
        print("not enough alliances or something went wrong.")
    #Hanhiho marks
    if (Hanjiho_counter >= 5):
        THC = THC + 1
    if (Hanjiho_counter >= 10):
        THC = THC + 1
    if (Hanjiho_counter >= 25):
        THC = THC + 1
    if (Hanjiho_counter >= 50):
        THC = THC + 1

    #studied in the awy
    if Endstudied == True:
        THC = THC + 1
    print(Endstudied)
    print('final score = ' + str(THC))
    return(THC)


