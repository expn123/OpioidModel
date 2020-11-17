import numpy as np
'''
class Costs:
    def __init__(self):
        self.cost = 0
    def get_costs(self,id,state):
        np.random.seed(id)
        if state==0:
            self.cost =np.random.gamma(16, 15.8625) + 30* np.random.gamma(16, 7.059375)
        if state==1:
            self.cost=0+30* np.random.gamma(16, 7.059375)
        if state==2:
            self.cost=0
        if state==3:
            self.cost=0
        if state==4:
            self.cost=np.random.gamma(16, 0.888125)*30
        if state==5:
            self.cost=0
        if state==6:
            self.cost=0
        if state==7:
            self.cost=0
        if state==8:
            self.cost=np.random.gamma(16, 73.4375)
        return self.cost
'''

class Costs:
    def __init__(self):
        self.cost = 0
    def get_costs(self,id,state):
        np.random.seed(id)
        if state==0:
            self.cost =np.random.gamma(400, 0.6345) + 30* np.random.gamma(400, 0.282375)
        if state==1:
            self.cost=0+30* np.random.gamma(400, 0.282375)
        if state==2:
            self.cost=0
        if state==3:
            self.cost=0
        if state==4:
            self.cost=np.random.gamma(400, 0.035525)*30
        if state==5:
            self.cost=0
        if state==6:
            self.cost=0
        if state==7:
            self.cost=0
        if state==8:
            self.cost=np.random.gamma(400, 2.9375)
        return self.cost

#updated: 08/24/2020：
class Utilites:
    def __init__(self):
        self.utility = 0
    def get_utility(self,id,state):
        np.random.seed(id)
        if state==0:
            self.utility=(1-np.random.gamma(1225, 0.0002857143))/12
        if state==1:
            self.utility=(1-np.random.gamma(1521, 0.0002564103))/12
        if state==2:
            self.utility=(1-np.random.gamma(841, 0.0003448276))/12
        if state==3:
            self.utility=(1-np.random.gamma(1089, 0.0003030303))/12
        if state==4:
            self.utility=(1-np.random.gamma(44.44444, 0.0045))/12
        if state==5:
            self.utility=(1-np.random.gamma(841, 0.0003448276))/12
        if state==6:
            self.utility=(1-np.random.gamma(1089, 0.0003030303))/12
        if state==7:
            self.utility=0
        if state==8:
            self.utility=(1-np.random.gamma(1089, 0.0003030303))/12
        return self.utility


