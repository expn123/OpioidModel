import psa_states as States

def matrix_gen(id):
    incar = States.transmatrixincar(id)
    row0 = incar[0]
    row1=incar[1]
    post_release=States.transmatrixpostrelease(id)
    row2 = post_release[0]
    row3 = post_release[1]
    row4 = States.transmatrixcommunitytreatment(id)
    row5 = States.transmatrixabstin(id)
    row7 = [0,0,0,0,0,0,0,1,0]
    row8 = [0,0,0,0,0,0,1,0,0]

    trans_matrix =[row0,row1,row2,row3,row4,row5,[],row7,row8]
    return trans_matrix

