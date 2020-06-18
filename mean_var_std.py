import numpy as np

def calculate(list):

  if len(list)<9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array(list).reshape(3,3)

  calc_dict = {}

  calc_dict['mean'] = [np.mean(arr, axis=0).tolist(),np.mean(arr, axis=1).tolist(), np.mean(arr)]

  calc_dict['variance'] = [np.var(arr, axis=0).tolist(),np.var(arr, axis=1).tolist(), np.var(arr)]

  calc_dict['standard deviation'] = [np.std(arr, axis=0).tolist(),np.std(arr, axis=1).tolist(), np.std(arr)]

  calc_dict['max'] = [np.amax(arr, axis=0).tolist(),np.amax(arr, axis=1).tolist(), np.amax(arr)]

  calc_dict['min'] = [np.amin(arr, axis=0).tolist(),np.amin(arr, axis=1).tolist(), np.amin(arr)]

  calc_dict['sum'] = [np.sum(arr, axis=0).tolist(),np.sum(arr, axis=1).tolist(), np.sum(arr)]

  return calc_dict
    