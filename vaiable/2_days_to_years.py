#days to years ,momths and days
days =int(input("Enter the number of days: "))
years = days // 365
remaining_days = days % 365
months = remaining_days // 30
final_days = remaining_days % 30
print(f"{years} years, {months} months, and {final_days} days")
