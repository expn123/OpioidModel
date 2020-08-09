import MarkovModelPsa as Model
import DataInput as Data
import numpy as np
"""
cohorta = Model.Cohort(id=20,n=3000,group=0)
cohorta.simulate(60)
cohortb = Model.Cohort(id=20,n=3000,group=1)
cohortb.simulate(60)
ICER = (cohorta.totalcost - cohortb.totalcost) / (cohorta.totalutility - cohortb.totalutility)



print(ICER)
print(cohorta.trans_matrix)
"""

m=Model.Multi_Cohort(1,1000)
m.simulate(60)
print(m._ICER)
print(m.dom)
