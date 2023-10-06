import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("Input list must contain exactly 9 digits.")
    
    matrix = np.array(lst).reshape(3, 3)
    
    result = {
        'mean': {
            'row': matrix.mean(axis=0).tolist(),
            'column': matrix.mean(axis=1).tolist(),
            'element': matrix.mean(),
        },
        'variance': {
            'row': matrix.var(axis=0).tolist(),
            'column': matrix.var(axis=1).tolist(),
            'element': matrix.var(),
        },
        'standard deviation': {
            'row': matrix.std(axis=0).tolist(),
            'column': matrix.std(axis=1).tolist(),
            'element': matrix.std(),
        },
        'max': {
            'row': matrix.max(axis=0).tolist(),
            'column': matrix.max(axis=1).tolist(),
            'element': matrix.max(),
        },
        'min': {
            'row': matrix.min(axis=0).tolist(),
            'column': matrix.min(axis=1).tolist(),
            'element': matrix.min(),
        },
        'sum': {
            'row': matrix.sum(axis=0).tolist(),
            'column': matrix.sum(axis=1).tolist(),
            'element': matrix.sum(),
        }
    }
    
    return result