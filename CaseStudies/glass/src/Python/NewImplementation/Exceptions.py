## @file Exceptions.py
#  @brief File that contains Exceptions.
#  @date 07/25/2018


## @brief An exception class for IndepVarNotAscending Exception
class IndepVarNotAscending(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

## @brief An exception class for SeqSizeMismatch
class SeqSizeMismatch(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

## @brief An exception class for InvalidInterpOrder
class InvalidInterpOrder(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

## @brief An exception class for OutOfDomain
class OutOfDomain(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

## @brief An exception class for InvalidIndex
class InvalidIndex(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)