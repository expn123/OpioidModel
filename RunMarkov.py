import MarkovModel as Model
import DataInput as Data
import numpy as np

'''
patient = Model.Patient(2,Data.trans_matrix_pr,group=0)
patient.simulate(Data.n_time_steps)
print( patient._outcomes.statecollection)
print(patient._death, patient._odcase)
print(patient._reincar)
'''
'''
print(sum(Data.trans_matrix_pr[8]))
'''
'''
od_treatment = []
od_control = []
incar_treatment =[]
incar_control = []
FATAL__treatment=[]
FATAL__control=[]


for i in range(0,100):
    cohorta = Model.Cohort(id=i,n=660,group=0)
    cohorta.simulate(20)
    cohortb = Model.Cohort(id=i, n=904, group=1)
    cohortb.simulate(23)
    od_treatment.append(cohorta.total_cases())
    od_control.append(cohortb.total_cases())
    incar_treatment.append(cohorta.total_reincar())
    incar_control.append(cohortb.total_reincar())
    FATAL__treatment.append(cohorta.get_mortality())
    FATAL__control.append(cohortb.get_mortality())

    print(i)

print(np.average(od_treatment),np.average(od_control),np.average(incar_treatment),np.average(incar_control))
print(np.average(FATAL__treatment),np.average(FATAL__control))
'''

'''
cohorta = Model.Cohort(id=14,n=660,group=0)
cohorta.simulate(20)
cohortb = Model.Cohort(id=14,n=904,group=1)
cohortb.simulate(23)
ICER = (cohorta.totalcost - cohortb.totalcost) / (cohorta.totalutility - cohortb.totalutility)


print(cohorta.totalcost - cohortb.totalcost)
print(cohorta.totalutility - cohortb.totalutility)
print(cohorta.total_cases(),cohortb.total_cases())
print(cohorta.total_reincar(),cohortb.total_reincar())
print(ICER)
print(cohorta.get_mortality(),cohortb.get_mortality())
'''

m=Model.Multi_Cohort(1,300)
m.simulate(60)
print(np.percentile(m._ICER,5),np.percentile(m._ICER,50),np.percentile(m._ICER,95))
print(np.average(m._costtreatment),np.average(m._costcontrol))
print(np.average(m.utilitytreatment),np.average(m.utilitycontrol))


'''
a=[]
b=[]
c=[]
d=[]
for i in range(0,100):
    cohorta = Model.Cohort(id=i, n=1500, group=0)
    cohorta.simulate(30)
    cohortb = Model.Cohort(id=i, n=1500, group=1)
    cohortb.simulate(30)
    a.append(cohorta.total_cases())
    b.append(cohortb.total_cases())
    c.append(cohorta.total_reincar())
    d.append(cohortb.total_reincar())
    print(i)
print(a,b,c,d)

print(np.average(a),np.average(b),np.average(c),np.average(d))
'''
