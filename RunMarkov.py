import MarkovModel as Model
import DataInput as Data
import numpy as np

'''
patient = Model.Patient(2,Data.trans_matrix_pr,group=0)
patient.simulate(Data.n_time_steps)
print( patient._outcomes.statecollection)
print(patient._death, patient._odcase)
'''
'''
print(sum(Data.trans_matrix_pr[8]))
'''
'''
cohorta = Model.Cohort(id=2,n=3000,group=0)
cohorta.simulate(36)
cohortb = Model.Cohort(id=2,n=3000,group=1)
cohortb.simulate(36)
ICER = (cohorta.totalcost - cohortb.totalcost) / (cohorta.totalutility - cohortb.totalutility)


print(cohorta.totalcost - cohortb.totalcost)
print(cohorta.totalutility - cohortb.totalutility)
print(cohorta.total_cases(),cohortb.total_cases())
print(cohorta.total_reincar(),cohortb.total_reincar())
'''

m=Model.Multi_Cohort(1,20)
m.simulate(60)
print(np.percentile(m._ICER,5),np.percentile(m._ICER,50),np.percentile(m._ICER,95))
print(m._cost,m._utlity)
