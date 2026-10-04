"""
condition inside condition called nested condition
is a situation where you place an additional
(if or else) statement inside an existing if or else block
"""
is_student = True
has_monthly_pass = False

#primery condition
if is_student:
    print("The user is a student!")

    #nested condition
    if has_monthly_pass:
        print("You get 30% discount!")
    else:
        print("You get 15% discount!")
else:
    print("The user isn\'t student!")
