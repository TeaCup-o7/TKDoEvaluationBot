#test = ['tester', 'Completed 612 minor quests','cheese','cake']

def first_substring(strings, substring):
    try:
        return min(i for i, string in enumerate(strings) if substring in string)
    except ValueError:
        print("No Mqs found")

def mqtest(test): #Tests MQ count
    try:
        index = first_substring(test,'minor quests')
        mq_mark = test[index]
        mq_count = test[index].split(' ')

        Tsteps = 0

        if (int(mq_count[1]) >= 10):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 25):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 50):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 100):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 250):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 500):
            Tsteps = Tsteps + 1
        if (int(mq_count[1]) >= 1000):
            Tsteps = Tsteps + 1
    except:
        Tsteps = 0
        mq_mark = "No Minor quests mark found!"
    return (Tsteps, mq_mark)

