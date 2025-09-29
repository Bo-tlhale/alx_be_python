from datetime import datetime, date,  timedelta

current_date = datetime.now()
print(f"Current date and time: {current_date}")

num_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = current_date + timedelta(num_of_days)
future_year = future_date.year
future_month = future_date.month
future_day = future_date.day
print(f"Future date: {future_year}-{future_month}-{future_day}")