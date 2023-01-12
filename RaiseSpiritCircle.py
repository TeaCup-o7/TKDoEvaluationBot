import DbManager as dbm
import exceptionRecorder as er
def checkKarma(content):
    check = str(content.person.lower())
    try:
        check = dbm.checkKarma(check)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            reward = 0
            RSCmsg1 = "Karma for {} has not been added to my records.".format(content.charName)
            RSCmsg2 = "Karma needs to be added to my records. \nTo update karma say: !add karma [name] [karma level]"
            #er.evalExcHandler(content)
            
            return(reward, RSCmsg1, RSCmsg2)
    karmaDic = dbm.getKarmaDic()
    reward = karmaDic[check[0].lower()]
    RSCmsg1 = "{} of 6.".format(reward)
    RSCmsg2 = "Karma level is {}. Last recorded by {} on {}.".format(check[0], check[1], check[2])
    return(reward, RSCmsg1, RSCmsg2)