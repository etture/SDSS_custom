import pandas as pd
from sklearn.metrics import log_loss
import pickle
import fire

rename_dict = {'STAR_WHITE_DWARF': 0, 'STAR_CATY_VAR':1, 'STAR_BROWN_DWARF':2,
       'SERENDIPITY_RED':3, 'REDDEN_STD':4, 'STAR_BHB':5, 'GALAXY':6,
       'SERENDIPITY_DISTANT':7, 'QSO':8, 'SKY':9, 'STAR_RED_DWARF':10, 'ROSAT_D':11,
       'STAR_PN':12, 'SERENDIPITY_FIRST':13, 'STAR_CARBON':14, 'SPECTROPHOTO_STD':15,
       'STAR_SUB_DWARF':16, 'SERENDIPITY_MANUAL':17, 'SERENDIPITY_BLUE':18}

def get_ground_truth(filename):
    pickle_in = open(filename,"rb")
    validate = pickle.load(pickle_in)
    validate2 = list()
    for v in validate:
        validate2.append(rename_dict[v])
    return validate2

def get_submission_file(filename):
    sub = pd.read_csv(filename)
    renamed = sub.rename(columns=rename_dict)
    return renamed

def get_score(sub_file, ground_truth_filename='ybigta_validate_full.pickle'):
    ground_truth = get_ground_truth(ground_truth_filename)
    submission = get_submission_file(sub_file)
    return log_loss(ground_truth, submission[submission.columns[1:]].values)

if __name__ == '__main__':
    fire.Fire(get_score)
