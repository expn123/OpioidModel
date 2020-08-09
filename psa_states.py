import numpy as np

#parameter sampling for state 0,1
#gamma distribution for duration of incarceration
incar_alpha = 44.05191
incar_beta = 4.153736


def transmatrixincar(id):
    np.random.seed(id)
    incar_dur = np.random.gamma(incar_alpha, incar_beta, size=1)
    rate_incar = 1 / (incar_dur[0] / 30)
    pr_remain = np.exp(-rate_incar)
    pr_release = 1-pr_remain
    trans_matrix = [[pr_remain,0,pr_release,0,0,0,0,0,0],[0,pr_remain,0,pr_release,0,0,0,0,0]]

    return trans_matrix


#prob transmatrix for state 5
#parameter sampling for reincarceration
reincar_alpha = 1359.703
reincar_beta = 0.3651343
#parameter sampling for resumption of drug use; (according to evidence, 90% for 6 months);fit a beta distribution for this probability. n=100
druguse_alpha = 89.1
druguse_beta = 9.9

def transmatrixabstin(id):
    np.random.seed(id)
    reincar_dur = np.random.gamma(reincar_alpha, reincar_beta, size=1)
    rate_reincar = 1 / (reincar_dur[0] / 30)

    prob_druguse = np.random.beta(a=druguse_alpha, b=druguse_beta, size=1)
    rate_druguse = -np.log(1 - prob_druguse[0]) / 6

    pr_remain = np.exp(-(rate_reincar+rate_druguse))
    pr_reincar = (1-pr_remain)*(rate_reincar/(rate_reincar+rate_druguse))
    pr_druguse = 1- pr_remain - pr_reincar
    trans_matrix = [0,pr_reincar,0,0,0,pr_remain,pr_druguse,0,0]

    return trans_matrix


#prob transmatrix for state 2,3
retreatment_alpha = 331.497
retreatment_beta = 327.503

recontrol_alpha = 103.885
recontrol_beta = 799.115

nonfatal_alpha= 0.9909091
nonfatal_beta= 108.0091

fatal_alpha = 7432.952
fatal_beta = 1967840

reintreatment_alpha = 25.96061
reintreatment_beta = 633.0394

reincontrol_alpha = 38.95686
reincontrol_beta = 864.0431

s = np.random.dirichlet((26.8,71.5),20)

def transmatrixpostrelease(id):
    np.random.seed(id)

    pr_resumptiontreatment = np.random.beta(retreatment_alpha,retreatment_beta,size=1)
    pr_resumptioncontrol = np.random.beta(recontrol_alpha,recontrol_beta,size=1)
    pr_nonfatal = np.random.beta(nonfatal_alpha,nonfatal_beta,size=1)
    pr_fatal = np.random.beta(fatal_alpha,fatal_beta,size=1)
    pr_reintreatment = np.random.beta(reintreatment_alpha,reintreatment_beta,size=1)
    pr_reincontrol = np.random.beta(reincontrol_alpha,reincontrol_beta,size=1)
    pr_treatment = 1-pr_resumptiontreatment[0]-pr_nonfatal[0]-pr_fatal[0]-pr_reintreatment[0]
    pr_control = 1-pr_resumptioncontrol[0]-pr_nonfatal[0]-pr_fatal[0]-pr_reincontrol[0]

    pr_otherstreatment = np.random.dirichlet((26.8,71.5),1)
    pr_otherscontrol = np.random.dirichlet((20.3,78.4),1)

    pr_treatmentabst = pr_treatment*pr_otherstreatment[0][0]/sum(pr_otherstreatment[0])
    pr_treatmentop = 1-pr_resumptiontreatment[0]-pr_nonfatal[0]-pr_fatal[0]-pr_reintreatment[0]-pr_treatmentabst
    pr_controlabst = pr_control*pr_otherscontrol[0][0]/sum(pr_otherscontrol[0])
    pr_controlop = 1-pr_resumptioncontrol[0]-pr_nonfatal[0]-pr_fatal[0]-pr_reincontrol[0]-pr_controlabst



    trans_matrix = [[pr_reintreatment[0],0,0,0,pr_resumptiontreatment[0],pr_treatmentabst,pr_treatmentop,pr_fatal[0],pr_nonfatal[0]],[0,pr_reincontrol[0],0,0,pr_resumptioncontrol[0],pr_controlabst,pr_controlop,pr_fatal[0],pr_nonfatal[0]]]

    return trans_matrix


#psa for state 4
retention_alpha = 111.8625
retention_beta = 5.8875
reinc_alpha = 10.50556
reinc_beta = 199.6056

def transmatrixcommunitytreatment(id):
    np.random.seed(id)

    pr_reinc = np.random.beta(reinc_alpha,reinc_beta)
    pr_retention = np.random.beta(retention_alpha,retention_beta)
    pr_reinc=pr_reinc
    pr_retention = (1-pr_reinc)*pr_retention

    pr_returntreatment = np.random.dirichlet((415,534),1)
    pr_reintreat = pr_reinc*pr_returntreatment[0][0]/sum(pr_returntreatment[0])
    pr_reincontrol = pr_reinc*pr_returntreatment[0][1]/sum(pr_returntreatment[0])

    pr_others = np.random.dirichlet((26.8,71.5),1)
    pr_abs = (1-pr_retention-pr_reinc)*pr_others[0][0]/sum(pr_others[0])
    pr_opioid = 1-pr_reinc-pr_retention-pr_abs

    trans_mat = [pr_reintreat, pr_reincontrol, 0, 0, pr_retention, pr_abs, pr_opioid, 0, 0]
    return trans_mat




