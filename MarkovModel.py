import DataInput as Data
from DataInput import HealthState

class Patient:
    def __init__(self,id,transition_matrix):
        """
        :param id: identification of each patient
        :param transition_matrix: probability transition matrix of different health states
        """
        self._id = id
        self._tranProb=transition_matrix
        self._healthstate = HealthState.Incar_MAT

    def simulate(self,n_time_steps):
        """simulate the patient over the specified simulation length"""

        k=0 #step counter;unit:month

        while k<n_time_steps:
            trans_prob = self._tranProb[self._healthstate.value] #a 'vector' of probabilities for a patient transfering to other states




