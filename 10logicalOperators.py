



has_high_income1 = True
has_good_credit1 = False

if has_high_income1 and has_good_credit1:
  print("eligible for loan 1")

# will not print if one of the condition is false




has_high_income2 = True
has_good_credit2 = True
if has_high_income2 or has_good_credit2:
  print("eligible for loan 2")



# also, try 'not' operator, example:
if has_high_income2 and not has_good_credit2:
  print("eligible for loan 3")
else:
  print("not eleigible for loan")