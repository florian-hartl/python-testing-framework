"""Functions to increment values or to set them to zero."""
import json


def zero():
  return 0


def inc(num):
  return num + 1


def zero_dict_values(data):
  """Sets values of input data to zero.

  Parameters
  ----------
  data : dict
    Any dictionary.
  """
  for k, v in data.items():
    data[k] = zero()


def inc_dict_values(data):
  """Increments values of input data.

  Parameters
  ----------
  data : dict
    A dictionary with numbers as values.
  """
  for k, v in data.items():
    data[k] = inc(v)


def inc_dict_objects(data):
  """Calls inc() method of all values of input data.

  Parameters
  ----------
  data : dict
    A dictionary with objects as values which have an inc() method.
  """
  for k, v in data.items():
    v.inc()


def inc_dict_values_from_file(path):
  """Reads a dict with numbers as values from file, increments the values,
  and writes the updated dict back to the same file, overriding the
  original one.

  Parameters
  ----------
  path : str
    Path to file, including filename.
  """
  data = read_json(path)
  inc_dict_values(data)
  write_json(path, data)


def read_json(path):
  """Reads a json file from disk.

  Parameters
  ----------
  path : str
    Path to file, including filename.
  """
  with open(path, 'r') as f:
    return json.load(f)


def write_json(path, data):
  """Writes data to a json file on disk.

  Parameters
  ----------
  path : str
    Path to file, including filename.
  data : anything compatible with json
    Data to be written to json file (string, list, dict, ...).
  """
  with open(path, 'w') as f:
    json.dump(data, f)
