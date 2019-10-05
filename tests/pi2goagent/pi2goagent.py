import bdiagent.bdiagent as agent
import simclient.simrobot as pi2go

class Pi2GoAgent(agent.Agent):
    def __init__(self):
        agent.Agent.__init__(self)

    def getpercepts(self, beliefbase):
        dist = 50
        beliefbase['distance'] = dist
        irR = pi2go.irRight()
        beliefbase['obstacle_right'] = irR
        irL = pi2go.irLeft()
        beliefbase['obstacle_left'] = irL
        irC = pi2go.irCentre()
        beliefbase['obstacle_centre'] = irC
        irLL = pi2go.irLeftLine()
        beliefbase['no_line_left'] = irLL
        irRL = pi2go.irRightLine()
        beliefbase['no_line_right'] = irRL
        switch = pi2go.getSwitch()
        beliefbase['switch_pressed']= switch
        lightFL = pi2go.getLightFL()
        beliefbase['lightFL'] = lightFL
        lightFR = pi2go.getLightFR()
        beliefbase['lightFR'] = lightFR
        lightBL = pi2go.getLightBL()
        beliefbase['lightBL'] = lightBL
        lightBR = pi2go.getLightBR()
        beliefbase['lightBR'] = lightBR
        super()
        return
        
    def run_agent(self):
        pi2go.init()
        super().run_agent()
        
    def cleanup(self):
        pi2go.cleanup()
        
        
