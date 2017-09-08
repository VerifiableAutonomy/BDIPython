import bdiagent

class Pi2GoAgent(bdiagent.Agent):

    def __init__(self):
        bdiagent.Agent.__init__(self)

    def getpercepts(self, beliefbase):
        dist = 50
        beliefbase['distance'] = dist
#		irR = robohat.irRight()
#		beliefbase['obstacle_right'] = irR
#		irL = robohat.irLeft()
#		beliefbase['obstacle_left'] = irL
#		irC = robohat.irCentre()
#		beliefbase['obstacle_centre'] = irC
#		irLL = robohat.irLeftLine()
#		beliefbase['no_line_left'] = irLL
#		irRL = robohat.irRightLine()
#		beliefbase['no_line_right'] = irRL
        switch = True
        beliefbase['switch_pressed']= switch
#        lightFL = robohat.getLightFL()
#        beliefbase['lightFL'] = lightFL
#        lightFR = robohat.getLightFR(0)
#        beliefbase['lightFR'] = lightFR
#		lightBL = robohat.getLightBL(0)
#		beliefbase['lightBL'] = lightBL
#		lightBR = robohat.getLightBR(0)
#		beliefbase['lightBR'] = lightBR
        super()
        return
