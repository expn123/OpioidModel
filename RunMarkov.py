import MarkovModel as Model
import DataInput as Data

'''
patient = Model.Patient(1,Data.trans_matrix_pr)
patient.simulate(Data.n_time_steps)
print(patient._outcomes.statecollection)
'''

cohorta = Model.Cohort(id=1,n=100,group=0)
cohorta.simulate(100)
cohortb = Model.Cohort(id=2,n=100,group=1)
cohortb.simulate(100)
ICER = (cohortb.totalcost - cohorta.totalcost) / (cohortb.totalutility - cohorta.totalutility)

print(cohorta.totalcost)

