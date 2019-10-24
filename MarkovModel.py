import DataInput as Data
from DataInput import HealthState
from DataInput import Costs
from DataInput import Utilites
import numpy as np


class Patient:
    def __init__(self,id,transition_matrix,group):
        """
        :param id: identification of each patient
        :param transition_matrix: probability transition matrix of different health states
        group: 0 means control group (without MAT), 1 means treatment group (with MAT)
        """
        self._id = id
        self._tranProb=transition_matrix
        self._group = group
        self._currentstate = HealthState(self._group) #current health state of the patient
        self._outcomes = Outcomes(self._id)

    def simulate(self,n_time_steps):
        """simulate the patient over the specified simulation length"""

        k=0 #step counter;unit:month

        while k<n_time_steps:
            # a 'vector' of probabilities for a patient transfering to other states:
            trans_prob = self._tranProb[self._currentstate.value]
            # updating the outcomes and health state of the patient:
            next_stateindex = np.random.choice(np.arange(len(trans_prob)),p=trans_prob)
            next_state = HealthState(next_stateindex)
            self._outcomes.update(self._currentstate,next_state)
            self._currentstate=next_state
            k=k+1

class Outcomes:
    def __init__(self,id):
        """
        :param id: this id should match the patient's id
        """
        self._id = id
        self._cost = 0
        self._utility = 0
        self.statecollection=[]
        self._reincacerated = 0
        self._commnutiytreatment = 0

        self.costinfo = Costs()
        self.utiinfo = Utilites()

    def update(self,current_state,next_state):
        #updating the costs of this patient:
        self._cost += self.costinfo.get_costs(current_state.value)
        # updating the utilities of this patient:
        self._utility += self.utiinfo.get_utility(current_state.value)
        #updating the state collection:
        self.statecollection.append(current_state.name)

        #reincacerated or not:
        if (current_state.value!=0 and current_state.value!=1) and (next_state.value==0 or next_state.value==1):
            self._reincacerated=1
        #get community treatment or not:
        if current_state.value == 2:
            self._commnutiytreatment=1

class Cohort:
    def __init__(self,id,n,group):
        """
        :param id: identification of the cohort
        :param n:number of patients in the cohort
        :param group:people in control or treatment group
        """
        self._id = id
        self._n = n #number of patients in the cohort
        self._group = group
        self.totalcost=0
        self.totalutility=0

    def simulate(self,n_time_steps):
        for i in range(0,self._n):
            patient = Patient(id=self._id*self._n+i,transition_matrix=Data.trans_matrix_pr,group=self._group)
            patient.simulate(n_time_steps)
            self.totalcost+=patient._outcomes._cost
            self.totalutility+=patient._outcomes._utility

    def get_average_costs(self):
        average_cost = sum(self.totalcost)/self._n
        return average_cost

    def get_average_utility(self):
        average_utility = sum(self.totalutility)/self._n
        return average_utility
















