import pi2goagent

agent = pi2goagent.Pi2GoAgent()

def print_switch_rule():
    switch_pressed = agent.sensor_value('switch_pressed')
    print("Switch Pressed: ", switch_pressed)
    return

agent.add_rule(print_switch_rule)
agent.run_agent()
