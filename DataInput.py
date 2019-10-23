import numpy as np
from enum import Enum
import pandas as pd

#probability transient matrix for different states
trans_matrix_pr = [
    [0,0,0.2,0.2,0.2,0.2,0.2],
    [0,0,0.2,0.2,0.2,0.2,0.2],
    [0.1,0.1,0,0.2,0.2,0.2,0.2],
    [0.1,0.1,0.2,0,0.2,0.2,0.2],
    [0.1,0.1,0.2,0.2,0,0.2,0.2],
    [0.1,0.1,0.2,0.2,0.2,0,0.2],
    [0.1,0.1,0.2,0.2,0.2,0.2,0],
]

class HealthState(Enum):
    """ health states of Individuals """
    Incar_MAT = 0 #people incarcerated with treatment program
    Incar_NoMAT = 1 #people incarcerated without treatment program
    MAT_NoIDU_Norx = 2 #people continue on treatment without IDU and pills
    No_MAT_NoIDU_Norx = 3  #people discontinue on treatment and drug free
    No_MAT_NoIDU_rx = 4 #people discontinue on treatment and without IDU but with pills
    No_MAT_IDU_Norx = 5 #people discontinue on treatment and with IDU but without pills
    No_MAT_IDU_rx = 6 #people discontinue on treatment and with IDU and with pills

#record the costs of each states
class Costs:
    def __init__(self):
        self.cost = 0
    def get_costs(self,state):
        if state==0:
            self.cost=200
        if state==1:
            self.cost=100
        if state==2:
            self.cost=200
        if state==3:
            self.cost=200
        if state==4:
            self.cost=200
        if state==5:
            self.cost=200
        if state==6:
            self.cost=200
        return self.cost


#record the utilities of each states
class Utilites:
    def __init__(self):
        self.utility = 0
    def get_utility(self,state):
        if state==0:
            self.utility=1
        if state==1:
            self.utility=1
        if state==2:
            self.utility=1
        if state==3:
            self.utility=1
        if state==4:
            self.utility=1
        if state==5:
            self.utility=1
        if state==6:
            self.utility=1
        return self.utility

#discount rates
discount_rate = 0.03

#length of simulation
n_time_steps=100
