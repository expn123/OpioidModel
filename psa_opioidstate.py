import numpy as np

treatmetn_shape = -1.259664
treatment_scale = 2.245558
treatment_cov = [[0.001535171,-0.000507225],[-0.000507225,0.02764602]]
treatment_mean = [-1.259664, 2.245558]

control_shape = -0.6618154
control_scale = 3.9872554
control_cov = [[0.00190032,-0.002139633],[-0.002139633,0.011440423]]
control_mean = [control_shape,control_scale]

od_shape = -0.6837627
od_scale = 8.5737476
od_cov = [[0.008810145,-0.04636014],[-0.046360143,0.28282073]]
od_mean = [od_shape,od_scale]

fatal_shape = -0.5452549
fatal_scale = 8.7789706
fatal_cov = [[0.01806808,-0.1063431],[-0.10634305,0.6951065]]
fatal_mean = [fatal_shape,fatal_scale]

#caculate lambda and scale (gamma)
#treatment
sample_treatment = np.random.multivariate_normal(treatment_mean, treatment_cov)
lambda_treatment = 1/np.exp(-sample_treatment[0])
gamma_treatment = np.exp(-sample_treatment[1]*lambda_treatment)
#control
sample_control = np.random.multivariate_normal(control_mean, control_cov)
lambda_control = 1/np.exp(-sample_control[0])
gamma_control = np.exp(-sample_control[1]*lambda_control)
#od
sample_od = np.random.multivariate_normal(od_mean, od_cov)
lambda_od = 1/np.exp(-sample_od[0])
gamma_od = np.exp(-sample_od[1]*lambda_od)
#fatal
sample_fatalod = np.random.multivariate_normal(fatal_mean, fatal_cov)
lambda_fatalod = 1/np.exp(-sample_fatalod[0])
gamma_fatalod = np.exp(-sample_fatalod[1]*lambda_fatalod)

#preparation for weillbul hazard
lambda_mat = [gamma_treatment, gamma_control]
scale_mat = [lambda_treatment, lambda_control]
lambda_nonfatal = gamma_od *3
scale_nonfatal = lambda_od
lambda_fatal = gamma_fatalod
scale_fatal = lambda_fatalod

rate_abstienence = 0.005
rate_reincarceration = 0.06



def weibull_rate(t,lamb,scale):
    rate = lamb * scale * pow(t,scale-1)
    return rate


def trans_matrixpr(t,group):
    # t: time; group: 1 is treatment, 0 is control
    rate_methadone = weibull_rate(t,lambda_mat[group],scale_mat[group])
    rate_nonfatal = weibull_rate(t,lambda_nonfatal,scale_nonfatal)
    rate_fatal = weibull_rate(t,lambda_fatal,scale_fatal)
    rate_sum = rate_methadone + rate_nonfatal + rate_fatal+rate_abstienence + rate_reincarceration

    #probability of stay
    pr_remain = np.exp(-rate_sum)
    pr_abstienence = (1-pr_remain)*(rate_abstienence/rate_sum)
    pr_methadone = (1-pr_remain)*(rate_methadone/rate_sum)
    pr_reincar = (1-pr_remain)*(rate_reincarceration/rate_sum)
    pr_fatal = (1-pr_remain)*(rate_fatal/rate_sum)
    pr_nonfatal = 1-pr_fatal-pr_reincar-pr_methadone- pr_abstienence-pr_remain

    #probability matrix
    trans_matrix = [0,pr_reincar,0,0,pr_methadone,pr_abstienence,pr_remain,pr_fatal,pr_nonfatal]
    return trans_matrix

print(trans_matrixpr(2,0))
