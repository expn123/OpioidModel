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
'''
trans_matrix_pr =[
    [0.848,0,0.152,0,0,0,0,0,0],
    [0,0.848,0,0.152,0,0,0,0,0],
    [0,0,0,0,0.503,0.132,0.352,0.003,0.01],
    [0,0,0,0,0.116,0.179141843971631,0.691858156028369,0.003,0.01],
    [0.021,0.029,0,0,0.9025,0.0129501525940997,0.0345498474059003,0,0],
    [0,0.0484506188071189,0,0,0,0.64146542082732,0.310083960365561,0,0],
    [],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0]

]
'''

#original matrix
trans_matrix_pr =[
    [0.848,0,0.152,0,0,0,0,0,0],
    [0,0.848,0,0.152,0,0,0,0,0],
    [0.0393939393939394,0,0,0,0.503,0.121215080612843,0.323390979993218,0.003,0.01],
    [0,0.043141592920354,0,0,0.116,0.170268750392268,0.657589656687378,0.003,0.01],
    [0.021,0.029,0,0,0.9025,0.0129501525940997,0.0345498474059003,0,0],
    [0,0.0484506188071189,0,0,0,0.64146542082732,0.310083960365561,0,0],
    [],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0]

]

'''
trans_matrix_pr =[
    [0.848,0,0.152,0,0,0,0,0,0],
    [0,0.848,0,0.152,0,0,0,0,0],
    [0.0393939393939394,0,0,0,0.503,0.121215080612843,0.323390979993218,0.003,0.01],
    [0,0.043141592920354,0,0,0.116,0.170268750392268,0.657589656687378,0.003,0.01],
    [0.021,0.029,0,0,0.855,0.0259003051881994,0.0690996948118006,0,0],
    [0,0.0484506188071189,0,0,0,0.64146542082732,0.310083960365561,0,0],
    [],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0]

]
'''
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
            self.cost=253.8+112.95*30
        if state==1:
            self.cost=0+112.95*30
        if state==2:
            self.cost=0
        if state==3:
            self.cost=0
        if state==4:
            self.cost=14.21*30
        if state==5:
            self.cost=0
        if state==6:
            self.cost=0
        if state==7:
            self.cost=0
        if state==8:
            self.cost=1175*(1-0.5)
        return self.cost


#record the utilities of each states
class Utilites:
    def __init__(self):
        self.utility = 0
    def get_utility(self,state):
        if state==0:
            self.utility=0.69/12
        if state==1:
            self.utility=0.640/12
        if state==2:
            self.utility=0.71/12
        if state==3:
            self.utility=0.67/12
        if state==4:
            self.utility=0.71/12
        if state==5:
            self.utility=0.8/12
        if state==6:
            self.utility=0.67/12
        if state==7:
            self.utility=0
        if state==8:
            self.utility=0.67/12
        return self.utility

#discount rates
discount_rate = 0.03/12

#length of simulation
n_time_steps=120

print(sum(trans_matrix_pr[3]))
