from bdiagent import Agent

class LogicAgent(Agent):

    def __init__(self):
        Agent.__init__(self)

    def getpercepts(self, beliefbase):
        choices = ['c1', 'c2', 'c3']
        beliefbase['choice'] = choices
        super()
        return
