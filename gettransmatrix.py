import DataInput as Data
import numpy as np

#rates
rate_abstienence = 0.005
rate_reincarceration = 0.06

#weibull parameters for treatment(0) and control(1)
lambda_mat = [0.53, 0.13]
scale_mat = [0.284, 0.52]
lambda_nonfatal = 0.013*3
scale_nonfatal = 0.50
lambda_fatal = 0.006
scale_fatal = 0.58


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

print(trans_matrixpr(2,1))
