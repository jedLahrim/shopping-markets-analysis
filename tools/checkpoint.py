import numpy as np


def checkpoint(file_name: str, checkpoint_header, checkpoint_data):
    np.savez(file_name, header=checkpoint_header, data=checkpoint_data)
    checkpoint_variable = np.load(file_name if ".npz" in file_name else file_name + '.npz')
    return checkpoint_variable
