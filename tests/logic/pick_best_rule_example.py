import logictestagent

agent = logictestagent.LogicAgent()

def mycmp(c1, c2):
    scores = agent.belief_value(agent.B('scores'))

    if scores[c1] > scores[c2]:
        return 1;
    else:
        return 0;


def print_choice_rule(choice):
    print (choice)
    return


agent.add_pick_best_rule(agent.B('choice'), mycmp, print_choice_rule)
agent.run_agent();

