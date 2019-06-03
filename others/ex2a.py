def bmr():
  w = float(input("what is your weight?"))
  g = input("what is your gender?")
  a = float(input("what is your age?"))
  h = float(input("what is your height?"))
  if g == "F":
    bmr = 655 + (4.3 * w) + (4.7 * h) - (4.7 * a)
  else:
    bmr = 66 + (6.3 * w) + (12.9 * h) - (6.8 * a)
  print(bmr)
