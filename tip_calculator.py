print("Welcome to the tip calculator.")

bill_total = float(input("What was the total bill? $"))
percent_choice = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_choice = int(input("How many people to split the bill? "))

bill_total_with_tip = (bill_total * (percent_choice / 100)) + bill_total

amt_per_person = round(bill_total_with_tip / split_choice, 2)
final_amount = "{:.2f}".format(amt_per_person)

print(f"Each person should pay: ${final_amount}")
