import MarkovModel as Model
import DataInput as Data

patient = Model.Patient(1,Data.trans_matrix_pr)
patient.simulate(Data.n_time_steps)

print(patient._outcomes.statecollection)
