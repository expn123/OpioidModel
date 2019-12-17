import numpy as np
from enum import Enum
import pandas as pd

#probability transient matrix for different states
'''
trans_matrix_pr =[ [
    [0.962470978,0,0,0.013510448,0.024018574,0,0],
    [0,0.962470978,0,0.009006965,0.028522057,0,0],
    [0.01161125,0.01161125,0.941617526,0.017579987,0.017579987,0,0],
    [0.011814071,0.011814071,0,0.975042573,0.001329285,0,0],
    [0.011250434,0.011250434,0.078363136,0.001085028,0.883135238,3.27613E-05,0.014882968],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0]
] ,
[
    [0.962470978,0,0,0.013510448,0.024018574,0,0],
    [0,0.962470978,0,0.009006965,0.028522057,0,0],
    [0.01161125,0.01161125,0.941617526,0.017579987,0.017579987,0,0],
    [0.011814071,0.011814071,0,0.975042573,0.001329285,0,0],
    [0.011523765,0.011523765,0.033241606,0.001111389,0.927321367,3.35573E-05,0.015244551],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0]
]
]
'''
trans_matrix_pr =[
    [0.847261533,0,0.152738467,0,0,0,0,0,0],
    [0,0.847261533,0,0.152738467,0,0,0,0,0],
    [0,0,0,0,0.518,0.096023556,0.370890987,0.00008545682,0.015],
    [0,0,0,0,0.118,0.178285767,0.6886287764,0.00008545682,0.015],
    [0.0015,0.0015,0,0,0.832,0.045,0.12,0,0],
    [00.0125,0.0125,0,0,0,0.969878623,0.005121377,0,0],
    [0.0165,0.0165,0,0,0.119167349,0.003984202,0.838370835,0.0000126178404274685,0.005464997],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0]

]

class HealthState(Enum):
    """ health states of Individuals """
    Incar_MAT = 0 #people incarcerated with treatment program
    Incar_NoMAT = 1 #people incarcerated without treatment program
    PostIncar_treatment =2
    PostIncar_control = 3
    MAT_NoIDU = 4 #people continue on treatment without IDU
    No_MAT_NoIDU = 5
    No_MAT_IDU = 6
    FatalOD = 7
    nonFatalOD = 8

#record the costs of each states
class Costs:
    def __init__(self):
        self.cost = 0
    def get_costs(self,state):
        if state==0:
            self.cost=8.46*30
        if state==1:
            self.cost=0
        if state==2:
            self.cost=14.21
        if state==3:
            self.cost=0
        if state==4:
            self.cost=0
        if state==5:
            self.cost=0
        if state==6:
            self.cost=0
        if state==7:
            self.cost=0
        if state==8:
            self.cost=1175
        return self.cost


#record the utilities of each states
class Utilites:
    def __init__(self):
        self.utility = 0
    def get_utility(self,state):
        if state==0:
            self.utility=0.685/12
        if state==1:
            self.utility=0.578/12
        if state==2:
            self.utility=0.67/12
        if state==3:
            self.utility=0.67/12
        if state==4:
            self.utility=0.71/12
        if state==5:
            self.utility=0.8/12
        if state==6:
            self.utility=0.67/12
        if state==7:
            self.utility=0.67/12
        if state==8:
            self.utility=0
        return self.utility

#discount rates
discount_rate = 0.03/12

#length of simulation
n_time_steps=120
