import traceback
import datetime as dt
template = '''
##########################################################
##########################################################
{}
Author: {}
Nick: {}
Target: {}
Content: {}
##########################################################\n'''
def getNow():
    date = dt.datetime.now()
    date = dt.datetime.strftime(date, '%h-%d-%Y_%H-%M-%S')

class evalExcHandler:
    def __init__(self, issue):
        self.date = dt.datetime.now()
        self.date = dt.datetime.strftime(self.date, '%h-%d-%Y_%H-%M-%S')
        f = open('{}{}.txt'.format('ErrorLog', self.date), 'w')
        f.write(template.format(self.date, issue.author, issue.nick, issue.person, issue.content))
        traceback.print_exc(file=f)
        f.close()

class basicHandler:
    def __init__(self):
        self.date = dt.datetime.now()
        self.date = dt.datetime.strftime(self.date, '%h-%d-%Y_%H-%M-%S')
        f = open('{}{}.txt'.format('ErrorLog', self.date), 'w')
        f.write(self.date + '\n')
        traceback.print_exc(file=f)
        f.close()
