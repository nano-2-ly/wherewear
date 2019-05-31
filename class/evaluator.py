class person_evaluator(object):
    def __init__(self, person):
        self.person = person

class environment_evaluator(object):
    def __init__(self, environment):
        self.environment = environment

class evaluator(object):
    def __init__(self, person, environment):
        self.person = person
        self.environment = environment
