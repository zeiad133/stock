def isPositiveNumber(input):
  str_input = str(input)
  if not str_input.isdigit():  return False
  return int(input) > 0
