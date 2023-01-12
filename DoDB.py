import sqlite3 as sql
import datetime as dt

def getNow(): #gets the current date in str format D M Y
    date = dt.datetime.now()
    date = dt.datetime.strftime(date, '%h-%d-%Y %H:%M CST')
    return(date)

def createDB():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS names
                    (n_tknick TEXT,
                    n_DiscordName TEXT UNIQUE NOT NULL,
                    PRIMARY KEY (n_DiscordName))''')  
    cur.execute('''CREATE TABLE IF NOT EXISTS names_log
                    (nl_action TEXT,
                    nl_tknick TEXT,
                    nl_DiscordName TEXT,
                    nl_date TEXT)''')
###########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS karma 
                    (k_name TEXT UNIQUE NOT NULL,
                    k_level TEXT,
                    k_updater TEXT,
                    k_date TEXT)''')
###########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS karma_log
                    (kl_name TEXT,
                    kl_newlevel TEXT,
                    kl_updater TEXT,
                    kl_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS tiger 
                    (t_name TEXT UNIQUE NOT NULL,
                    t_updater TEXT,
                    t_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS wisdom 
                    (w_name TEXT UNIQUE NOT NULL,
                    w_updater TEXT,
                    w_date TEXT)''')
###########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS secretmast 
                    (sm_name TEXT UNIQUE NOT NULL,
                    sm_updater TEXT,
                    sm_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS secondary 
                    (sec_name TEXT UNIQUE NOT NULL,
                    sec_updater TEXT,
                    sec_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS primaryf
                    (p_name TEXT UNIQUE NOT NULL,
                    p_updater TEXT,
                    p_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS weaponforms 
                    (wf_name TEXT UNIQUE NOT NULL,
                    wf_count TEXT,
                    wf_updater TEXT,
                    wf_date TEXT)''')
##########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS shield 
                    (sh_name TEXT UNIQUE NOT NULL,
                    sh_updater TEXT,
                    sh_date TEXT)''')
###########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS honor 
                    (h_name TEXT UNIQUE NOT NULL,
                    h_updater TEXT,
                    h_date TEXT)''')
###########################################################
    cur.execute('''CREATE TABLE IF NOT EXISTS solo 
                    (sf_name TEXT UNIQUE NOT NULL,
                    sf_updater TEXT,
                    sf_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS evals
                    (e_name TEXT,
                    e_tester TEXT,
                    e_status TEXT,
                    e_date)''')


    con.commit()
    con.close()

def dropAll():
    con = sql.connect('DoDB.db')
    con.execute('''DROP TABLE IF EXISTS names''')
    con.execute('''DROP TABLE IF EXISTS names_log''')
    con.execute('''DROP TABLE IF EXISTS karma''')
    con.execute('''DROP TABLE IF EXISTS karma_log''')
    con.execute('''DROP TABLE IF EXISTS tiger''')
    con.execute('''DROP TABLE IF EXISTS wisdom''')
    con.execute('''DROP TABLE IF EXISTS secretmast''')
    con.execute('''DROP TABLE IF EXISTS secondary''')
    con.execute('''DROP TABLE IF EXISTS primaryf''')
    con.execute('''DROP TABLE IF EXISTS weaponforms''')
    con.execute('''DROP TABLE IF EXISTS shield''')
    con.execute('''DROP TABLE IF EXISTS honor''')
    con.execute('''DROP TABLE IF EXISTS solo''')
    con.execute('''DROP TABLE IF EXISTS evals''')
    print("all tables dropped")
    con.close()


#name sql
def setName(discordName, tkName):
    namesList = getNamesDiscord()
    date = getNow()
    if str(discordName) not in namesList:
        con = sql.connect('DoDB.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO names (n_tknick, n_DiscordName) VALUES (?,?)''', (tkName, str(discordName)))
        cur.execute('''INSERT INTO names_log (nl_action, nl_tknick, nl_DiscordName, nl_date) VALUES (?,?,?,?)''', ('add', tkName, str(discordName), date))
    else:
        con = sql.connect('DoDB.db')
        cur = con.cursor()
        cur.execute('''UPDATE names SET n_tknick = ? WHERE n_DiscordName = ?''', (tkName, str(discordName)))
        cur.execute('''INSERT INTO names_log (nl_action, nl_tknick, nl_DiscordName, nl_date) VALUES (?,?,?,?)''', ('update', tkName, str(discordName), date))
        
    con.commit() 
    con.close()

def getNames():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT * FROM names''')
    cont = []
    for x in query:
        print(x)
    con.close()

def getNamesDiscord():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT n_DiscordName FROM names''')
    cont = []
    for x in query:
        cont.append(x[0])
    return(cont)

def getNamesByDiscord(discordName):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT n_tknick FROM names WHERE n_DiscordName = ?''', (discordName,))
    cont = []
    for x in query:
        cont.append(x[0])
    return(cont[0])

def getNamesReport():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT * FROM names''')
    cont = []
    for x in query:
        if x[1] == 'Slavell#8770':
            pass
        else:
            cont.append("{} as {}".format(x[1],x[0]))
    con.close()
    return(cont)

def getNamesLogReport():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT * FROM names_log''')
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    return(cont)

def setKarma(person, karma, discordName):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    date = getNow()
    try:
        cur.execute('''INSERT INTO karma (k_name, k_level, k_updater, k_date) VALUES (?,?,?,?)''', (person.lower(), karma.lower(), str(discordName), date))    
    except:
        cur.execute('''UPDATE karma SET k_level = ?, k_updater = ?, k_date = ? WHERE k_name = ?''', (karma.lower(), str(discordName), date, person.lower()))
    cur.execute('''INSERT INTO karma_log (kl_name, kl_newlevel, kl_updater, kl_date) VALUES (?, ?, ?, ?)''', (person.lower(), karma.lower(), discordName, date))
    con.commit()
    con.close()    

def getKarma(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT k_level, k_updater, k_date FROM karma WHERE k_name = ?''', (person,))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    level = cont[0][0]
    updater = cont[0][1]
    date = cont[0][2]
    return(level, updater, date)       

#print(getKarma('phillies'))

def getKarmaLog():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT * FROM karma_log''')
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    return(cont)    

def setTiger(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    try:
        cur.execute('''INSERT INTO tiger (t_name, t_updater, t_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    except:
        pass
    con.commit()
    con.close()

def getTiger(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT t_updater, t_date FROM tiger WHERE t_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 
################################
def setWisdom(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO wisdom (w_name, w_updater, w_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getWisdom(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT w_updater, w_date FROM wisdom WHERE w_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 
##############################
def setSecretMastery(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO secretmast (sm_name, sm_updater, sm_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getSecretMastery(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT sm_updater, sm_date FROM secretmast WHERE sm_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setSecondaryForms(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO secondary (sec_name, sec_updater, sec_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getSecondaryForms(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT sec_updater, sec_date FROM secondary WHERE sec_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setPrimary(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO primaryf (p_name, p_updater, p_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getPrimary(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT p_updater, p_date FROM primaryf WHERE p_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setWeaponForms(person, count, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    try:
        cur.execute('''INSERT INTO weaponforms (wf_name, wf_count, wf_updater, wf_date) VALUES (?,?,?,?)''', (str(person.lower()), str(count), str(discordName), date))  
    except:
        cur.execute('''UPDATE weaponforms SET wf_count = ?, wf_updater = ?, wf_date = ? WHERE wf_name = ?''', (str(count), str(discordName), date, str(person.lower())))
    con.commit()
    con.close()

def getWeaponForms(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT wf_updater, wf_date, wf_count FROM weaponforms WHERE wf_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    count = cont[0][2]
    return(count, updater, date) 
#weaponforms

def setShield(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO shield (sh_name, sh_updater, sh_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getShield(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT sh_updater, sh_date FROM shield WHERE sh_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setHonor(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO honor (h_name, h_updater, h_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getHonor(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT h_updater, h_date FROM honor WHERE h_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setSolo(person, discordName):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO solo (sf_name, sf_updater, sf_date) VALUES (?,?,?)''', (str(person.lower()), str(discordName), date))  
    con.commit()
    con.close()

def getSolo(person):
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT sf_updater, sf_date FROM solo WHERE sf_name = ?''', (str(person.lower()),))
    cont = []
    for x in query:
        cont.append(x)
    con.close()
    updater = cont[0][0]
    date = cont[0][1]
    return(updater, date) 

def setEval(person, discordName, status):
    date = getNow()
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO evals (e_name, e_tester, e_status, e_date) VALUES (?,?,?,?)''', (str(person.lower()), str(discordName), status, date))
    con.commit()
    con.close()

def getEvalCount():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT count(*) FROM evals WHERE e_status = ?''', ('Pass',))
    count = 0
    for x in query:
        count = x[0]
    con.close()
    return(count)
    
#dropAll()
createDB()


def specialTest():
    con = sql.connect('DoDB.db')
    cur = con.cursor()
    query = cur.execute('''SELECT * FROM shield''')
    cont = []
    for x in query:
        print(x)
    con.close()
    return(cont)  
#specialTest()
