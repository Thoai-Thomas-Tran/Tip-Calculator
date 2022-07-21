print("Welcome to the tip calculator.")

bill_total = input("What was the total bill? $")
percent_choice = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_choice = input("How many people to split the bill? ")

float_bill_total = float(bill_total)
int_percent_choice = int(percent_choice)
int_split_choice = int(split_choice)
tip_total = float_bill_total * (int_percent_choice / 100)

amt_per_person = round((tip_total + float_bill_total) / int_split_choice, 2)

print(f"Each person should pay: ${amt_per_person}")
