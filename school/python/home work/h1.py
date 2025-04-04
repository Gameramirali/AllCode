days_in_year = 365
days_in_week = 7
input_days = int(input("Please enter the number of days: "))
years = input_days // days_in_year
remaining_days = input_days % days_in_year
weeks = remaining_days // days_in_week
days = remaining_days % days_in_week
print(f"{input_days} day == year={years},week={weeks},days={days}")