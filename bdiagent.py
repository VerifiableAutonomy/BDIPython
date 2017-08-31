import time

class Agent:
	
    def __init__(self):
        self.beliefbase = {}
        self.rules = {}
        self.num_rules = 0
        self.running = 0
        # list of goal names
        self.goalbase = []
        # dictionary linking goal names to functions that determine if they are satisfied
        self.goal_functions = {}
        self.pending_goals = {}


    # REASONING CYCLE
    def run_agent(self):
        # robohat.init()
        self.running = 1
        # dummy_rule is a catch all if no other rule applies
        self.add_rule(self.dummy_rule)
        while (self.running):
            self.reason()
    
    def reason(self,robot,rule_info):
#        self.getpercepts(self.beliefbase)
        self.manage_goals(self.beliefbase, self.goalbase)
        selected_rule = self.selectRule(self.beliefbase, self.goalbase)
        self.execute(selected_rule, robot, rule_info)

#==============================================================================
#     def getpercepts(self, beliefbase):
# 		time.sleep(0.1)
# 		return
# 
#==============================================================================
    def manage_goals(self, beliefbase, goalbase):
        for goal in self.goalbase:
            if (self.is_achieved(goal)):
                print goal, " Goal Achieved!"
                self.achieved_goal(goal, goalbase)
        return

    # A goal is achieved if either it shares a name with a belief and the belief is true or its associated function returns true
    def is_achieved(self, goal):
        if (goal in self.beliefbase.keys()):
            if (self.beliefbase[goal] == 1):
                return 1
            return 0
        else:
            goalfunc = self.goal_functions[goal]
            if (goalfunc()):
                return 1
            return 0

    #  When a goal is achieved it is removed from the goalbase, if it is a subgoal of some other goal then the next subgoal should now be attempted
    def achieved_goal(self, goal, goalbase):
        goalbase.remove(goal)
        if (goal in self.pending_goals.keys()):
            next_goallist = self.pending_goals[goal]
            next_goal = next_goallist.pop(0)
            self.add_goal(next_goal)
            self.pending_goals.pop(goal, None)
            if (len(next_goallist) > 0):
                self.pending_goals[next_goal] = next_goallist
        return

    def selectRule(self, beliefbase, goalbase):
        for key in self.rules.keys():
            tuple = self.rules[key]
            guard = tuple[0]
            if (guard() == 1):
                selected_rule = tuple[1]
                return selected_rule

    def execute(self, rule, robot, rule_info):
        rule(robot, rule_info)
    
    # REASONING ABOUT BELIEFS
    # believe and B are the same.
    def believe(self, key):
        return lambda: self.believe_support(key, self.beliefbase)
        
    def B(self, key):
        return lambda: self.believe_support(key, self.beliefbase)
        
    def believe_support(self, key, beliefbase):
        print ('checking ' ), key
        if (key in beliefbase):
            return beliefbase[key]
        return 0
                    
    def AND(self, belief1, belief2):
        return lambda: self.and_support(belief1, belief2)
                            
    def and_support(self, belief1, belief2):
        if (belief1() == 1):
            return belief2()
        else:
            return 0
        
    def NOT(self, belief):
        return lambda: self.not_support(belief)
        
    def not_support(self, belief):
        if (belief() == 1):
            return 0
        else:
            return 1
        
    def OR(self, belief1, belief2):
        return lambda: self.or_support(belief1, belief2)
        
    def or_support(self, belief1, belief2):
        if (belief1() == 1):
            return 1
        else:
            return belief2()


    # REASONING ABOUT GOALS - NB Think AND, OR, NOT etc will also work for goals but haven't checked this.
    # has_goal and G are the same
    def has_goal(self, key):
		return lambda: self.goal_support(key, self.goalbase)

    def G(self, key):
		return lambda: self.goal_support(key, self.goalbase)

    def goal_support(self, key, goalbase):
		if (key in goalbase):
			return 1
		return 0

    # RULES
    def add_rule(self, rule):
        self.rules[self.num_rules] = (self.alwaystrue, rule)
        self.num_rules = self.num_rules + 1
        
    def add_condition_rule(self, condition, rule):
        self.rules[self.num_rules] = (condition, rule)
        self.num_rules = self.num_rules + 1


    # Functions for inclusion in rules
    def sensor_value(self, key):
        if (key in self.beliefbase):
            return self.beliefbase[key]
        else:
            print ("ERROR: No value from sensors for ", key)
            return 0

    def done(self):
        self.running = 0;
        
    #  BELIEF MANAGEMENT
    def add_belief(self, key):
		self.beliefbase[key] = 1
    
    def drop_belief(self, key):
        self.beliefbase[key] = 0

    def change_belief(self, key, value):
		self.beliefbase[key] = value

    #  GOAL MANAGEMENT
    def add_goal(self, key):
		self.goalbase.append(key)

    def add_subgoals(self, goal, goallist):
        first_goal = goallist.pop(0)
        self.add_goal(first_goal)
        self.pending_goals[first_goal] = goallist

    def drop_goal(self, key):
        self.goalbase.remove(key)

    def goal_is_achieved_when(self, key, function):
        self.goal_functions[key] = function

    # Default Rule
    def alwaystrue(self):
        return 1

    def dummy_rule(self, plan, robot):
         time.sleep(0.5)
         return

