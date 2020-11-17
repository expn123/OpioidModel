import DataInput as Data
from DataInput import HealthState
from DataInput import Costs
from DataInput import Utilites
import numpy as np
from gettransmatrix import trans_matrixpr


class Patient:
    def __init__(self,id,transition_matrix,group):
        """
        :param id: identification of each patient
        :param transition_matrix: probability transition matrix of different health states
        group: 0 means treatment group (with MAT), 1 means treatment group (without MAT)
        """
        self._id = id
        self._group = group #treatment or control group
        self._tran=transition_matrix
        self._currentstate = HealthState(self._group) #current health state of the patient
        self._outcomes = Outcomes(self._id)
        self._death = 0
        self._odcase=0
        self._reincar = 0
        self._resumption=0
        self._release =0
        self._trelase = 0
        self._releasetime = 0


    def simulate(self,n_time_steps):
        """simulate the patient over the specified simulation length"""

        k=0 #step counter;unit:month

        while k<n_time_steps:
            if self._currentstate.value!=6:
                # a 'vector' of probabilities for a patient transfering to other states:
                trans_prob = self._tran[self._currentstate.value]
            if self._currentstate.value==6:
                trans_prob = trans_matrixpr(k-self._releasetime+1,self._group)
            # updating the outcomes and health state of the patient:
            next_stateindex = np.random.choice(np.arange(len(trans_prob)),p=trans_prob)
            next_state = HealthState(next_stateindex)

            if self._currentstate.value==7:
                self._death=1

            if self._currentstate.value==8:
                self._odcase+=1

            if self._currentstate.value==0:
                self._group=0

            if self._currentstate.value==1:
                self._group = 1

            if self._currentstate.value==2 or self._currentstate.value==3:
                self._release =1
                self._releasetime = k

            if (self._currentstate.value!=0 and self._currentstate.value!=1) and (next_stateindex==0 or next_stateindex==1):
                self._reincar +=1
            k=k+1

            self._outcomes.update(self._currentstate,next_state,k)
            self._currentstate=next_state

class Outcomes:
    def __init__(self,id):
        """
        :param id: this id should match the patient's id
        """
        self._id = id
        np.random.seed(id)
        self._cost = 0
        self._utility = 0
        self.statecollection=[]
        self._reincacerated = 0
        self._commnutiytreatment = 0

        self.costinfo = Costs()
        self.utiinfo = Utilites()

    def update(self,current_state,next_state,time):
        #updating the costs of this patient:
        self._cost += self.costinfo.get_costs(current_state.value)/(1+Data.discount_rate)**time
        # updating the utilities of this patient:
        self._utility += self.utiinfo.get_utility(current_state.value)/(1+Data.discount_rate)**time
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
        self._deaths=[]
        self._cases=[]
        self._reincar=[]

    def simulate(self,n_time_steps):
        for i in range(0,self._n):
            patient = Patient(id=self._id*self._n+i,transition_matrix=Data.trans_matrix_pr,group=self._group)
            patient.simulate(n_time_steps)
            self.totalcost+=patient._outcomes._cost
            self.totalutility+=patient._outcomes._utility
            self._deaths.append(patient._death)
            self._cases.append(patient._odcase)
            self._reincar.append(patient._reincar)

    def get_average_costs(self):
        average_cost = sum(self.totalcost)/self._n
        return average_cost

    def get_average_utility(self):
        average_utility = sum(self.totalutility)/self._n
        return average_utility

    def get_mortality(self):
        mortality = sum(self._deaths)
        return mortality

    def total_cases(self):
        total_case = sum(self._cases)
        return total_case
    def total_reincar(self):
        total = sum(self._reincar)
        return total



class Multi_Cohort:
    def __init__(self, id, n):
        """
        :param id: identification of the cohort
        :param n:number of patients in the cohort
        :param group:people in control or treatment group
        """
        self._id = id
        self._n = n  # number of patients in the cohort
        self._ICER=[]
        self._cost=[]
        self._utlity=[]
        self._incara=[]
        self._incarb=[]
        self._casea=[]
        self._caseb=[]
        self._costtreatment = []
        self._costcontrol = []
        self.utilitytreatment=[]
        self.utilitycontrol=[]

    def simulate(self, n_time_steps):
        for i in range(0, self._n):
            cohorta = Cohort(id=self._id*self._n+i, n=3000, group=0)
            cohorta.simulate(n_time_steps)
            cohortb = Cohort(id=self._id*self._n+i, n=3000, group=1)
            cohortb.simulate(n_time_steps)
            ICER = (cohorta.totalcost - cohortb.totalcost) / (cohorta.totalutility - cohortb.totalutility)
            self._ICER.append(ICER)
            self._costtreatment.append(cohorta.totalcost )
            self._costcontrol.append(cohortb.totalcost )
            self.utilitytreatment.append(cohorta.totalutility)
            self.utilitycontrol.append(cohortb.totalutility)

            self._incara.append(cohorta.total_reincar())
            self._incarb.append(cohortb.total_reincar())
            self._casea.append(cohorta.total_cases())
            self._caseb.append(cohortb.total_cases())
            print(i)
