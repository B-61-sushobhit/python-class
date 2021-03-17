# to check whether the year is an leap year or not an leap year
y = int(input("enter the year"))
if y%4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("yes it is an leap year")
        else:
            print("no")
    else:
        print("yes it is an leap year")
else:
    print("no")
