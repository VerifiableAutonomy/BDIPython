import pi2goagent

agent = pi2goagent.Pi2GoAgent()

def print_switch_rule():
	print ("Switch Pressed: ", agent.sensor_value('switch_pressed'))
	return

agent.add_rule(print_switch_rule)
agent.run_agent()
