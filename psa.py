import numpy as np

#parameter sampling for state 0,1
#gamma distribution for duration of incarceration
incar_alpha = 44.05191
incar_beta = 4.153736


def transmatrixincar(id,group):
    np.random.seed(id)
    incar_dur = np.random.gamma(incar_alpha, incar_beta, size=1)
    rate_incar = 1 / (incar_dur[0] / 30)
    pr_remain = np.exp(-rate_incar)
    pr_release = 1-pr_remain
    trans_matrix = [[pr_remain,0,pr_release,0,0,0,0,0,0],[0,pr_remain,0,pr_release,0,0,0,0,0]]

    return trans_matrix[group]


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

