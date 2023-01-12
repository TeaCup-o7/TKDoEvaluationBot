import numpy as np

def Search(strings, substring):
    try:
        return min(i for i, string in enumerate(strings) if substring in string)
    except ValueError:
        np.ERR_IGNORE
    return