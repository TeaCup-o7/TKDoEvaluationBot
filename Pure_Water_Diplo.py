import MarkFinder
########################
#START DIPLOMACY SECTION
########################

#count=7
Ranger = ['level in Archer (Marked by', #substring added 4/4/23
          'level in Camouflage (Marked by', #substring added 4/4/23
          'level in Cartography (Marked by', #substring added 4/4/23
          'level in Foraging (Marked by', #substring added 4/4/23
          'level in Security (Marked by', #substring added 4/4/23
          'level in Tracking (Marked by', #substring added 4/4/23
          'level in Trapping (Marked by'] #substring added 4/4/23

#count=15
Diviner = ['Found Serenity in the Tao', 
           'Fortune revealed', 
           'rituals of Divinity', 
           'Contributor of Joy. Observed by',
            'Alignment of Yin and Yang',
            'Alignment of Yang', 
            'Alignment of Yin', 
            'Born under the', #Born under the is zodiac reveal
            'Saw the vision of Kujiga',
            'Purified Marriage, blessed by', 
            'Swore oath to forsake all lies, witnessed',
            'Attained Tai-chi. Guided by', 
            'Wove the Threads of Fate, assisted by',
            'Born under the Earth Sheep, revealed by Milana in', 
            'Mastered their understanding of the']

#count=5
Geomancer = ['Forged an orb of', 
             'Wu Wei', 
             'Wu Xing' ,
             'Tiaoli', 
             'Learned to walk the neutral path, marked by'] #, 'Tiaoli Follower, Chosen by'] #this guy wasn't considering initiates

#count=3
Shaman = ['Kindred Spirits', 
          'Totem Spirit Revealed (Discovered by', 
          'Ascended through the Medicine Wheel']

#count=5
Druid = ['Recognized as Herbalist by Druid', 
         'Bard by Druid', 
         'Ovate by Druid ', 
         'Aided the Druids in the mystic garden',
         'Crafted a forgotten Druid artifact']

#count=12
Monk = ['Exerted Right Effort, recorded by', #replaced old substring on 4/4/23
        'Considered Right Mindfulness, recorded by', #replaced old substring on 4/4/23
        'Performed Right Action, recorded by', #replaced old substring on 4/4/23
        'Experienced Right Livelihood, recorded by', #replaced old substring on 4/4/23
        'Contemplated Right Thinking, recorded by', #replaced old substring on 4/4/23
        'Observed Right Views, recorded by', #replaced old substring on 4/4/23
        'Vocalized Right Speech, recorded by', #replaced old substring on 4/4/23
        'Reflected Right Meditation, recorded by', #replaced old substring on 4/4/23
        'in a Past Life, revealed by',
        'Walked the Eightfold path', 
        'Renewed marriage vows to', 
        'Devoted to raven, observed by Druid']

#count=9
Muse = ['Empowered with the Aura of the Muses', 
        'Professor of Muse College', 
        'Discovered Kaleidoscope of Life', 
        'Destined to break hearts', 
        'Dazzling Socialite',
        'Survived Girl', 
        'Caught Conspiring with Girl', 
        'Dabbled in the Dark Arts', 
        'Graduated Muse College']

#count=15
Merchant = ['Certified Treasure Hunter', 
            'Treasure Hunter, approved by', 
            'Mastered the art of Trading', 
            'Certified Economist', 
            'Discovered True Wealth', 
            'Preferred Client', 
            'Deemed Lucky, affirmed by', 
            'Demonstrated Duty to Path', 
            'Embodied Duty to Self', 
            'Exemplified Duty to Community', 
            'Devout follower of Kubera', 
            'Economist, approved by',
            'Ally of the Merchant Guild',
            'Recognized Collector, marked',
            'Lauded philanthropist, distinguished by']

#count=2
Spy = ['Associate of the Koguryian Spy Guild', 
       'Aided the KSG']

#count=4
Barbarian = ['Survived Wilderness training', 
             'Learned the ancient Sonhi art of the Throwing axe', 
             'Unearthed the Ancient Trails of the Wilderness', 
             'Sworn to the Horde']

#count=3
Chongun = ['Trained in the art of war,', 
           'Has demonstrated an understanding of honor', 
           'Mastered Heavenly Advance']

#count=8
Kingdoms = ['Benefactor of the Shining Jewel Foundation', 
            'Member of the Imperial Ministry of Buya', 
            'Member of the Royal Ministry of Koguryo',
            'Member of the Eternal Order of Nagnang?', 
            'Awarded High Myongye',
            'Affiliate of the Sovereign', 
            'Knighted with Royal Nobility', 
            'Resolved the Gogoon Family']


def PWC_Test(test,list):
    print("starting Diplomacy test")
    marks = []
    PWC = 0
    pos = 0
    Spos = 0
    while pos <= len(list)-1:
        try:
            bool, mark = MarkFinder.Mark_Test(test,list[pos])
            pos = pos + 1
            if bool == True:
                marks.append(mark[0])
                PWC = PWC + 1

            if list == Druid:
                if Spos == 0:
                    Spos = Spos + 1
                    print("testing special: animal devotion")
                    bool, mark = MarkFinder.Mark_Test(test, 'Devoted to')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[3] == 'observed':
                            print("test 1 passed")
                        if tmark[4] == 'by':
                            print("test 2 passed")
                        if tmark[5] == 'Druid':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        pass
            if list == Druid:
                if Spos == 1:
                    Spos = Spos + 1
                    print("testing special: elemental alignment")
                    bool, mark = MarkFinder.Mark_Test(test, 'Aligned with')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[3] == 'Recognized':
                            print("test 1 passed")
                        if tmark[4] == 'by':
                            print("test 2 passed")
                        if tmark[5] == 'Druid':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        pass
            if list == Druid:
                if Spos == 0:
                    Spos = Spos + 1
                    print("testing special: God Acolyte")
                    bool, mark = MarkFinder.Mark_Test(test, 'Acolyte of')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[3] == 'sworn':
                            print("test 1 passed")
                        if tmark[4] == 'by':
                            print("test 2 by")
                        if tmark[5] == 'Druid':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        pass    
            if list == Monk:
                if Spos == 2:
                    Spos = Spos + 1
                    print("testing special: Belong to family")
                    bool, mark = MarkFinder.Mark_Test(test, 'Member of the')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[4] == 'family':
                            print("test 1 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        pass
        except:
            pos = pos + 1
    if PWC > 2:
        PWC = 2
    return(PWC, marks)


def PWC_final(test):
    list = [Ranger, Diviner, Geomancer, Shaman, Druid, Monk, Muse, Merchant, Spy, Barbarian, Chongun, Kingdoms]
    pos = 0
    fPWC = 0
    diplo = 0
    markfound = []
    while pos <= len(list)-1:
        PWC, marks = PWC_Test(test, list[pos])
        markpos = 0
        while markpos < len(marks):
            markfound.append(marks[markpos])
            markpos = markpos + 1
        fPWC = fPWC + PWC
        pos = pos + 1
    if fPWC >= 5:
        diplo = diplo + 1
    if fPWC >= 10:
        diplo = diplo + 1
    return (diplo, markfound)


#PWC_final(test)
