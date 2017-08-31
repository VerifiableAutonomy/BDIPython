import logictestagent

agent = logictestagent.LogicAgent()

def print_choice(choice):
	print ("Choice is: ", choice)
	return

agent.add_condition_rule(x=agent.B('choice'), print_choice(x))
agent.run_agent()
