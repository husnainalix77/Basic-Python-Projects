beverages = ['Coffee', 'Tea', 'Coke', 'Orange Juice']
votes = [0] * len(beverages)
person_number = 1
count_person = 0

print("****************************************************************")
print("1. Coffee   2. Tea   3. Coke   4. Orange Juice")
print("****************************************************************")
print("Choose (1-4) from the above menu or 0 to exit the program.")

while True:
    try:
        op = int(input(f"Please input the favorite beverage of person #{person_number}: "))
    except ValueError:
        print("Please enter numbers only (1-4).")
        continue

    if 1 <= op <= len(beverages):
        votes[op - 1] += 1       # increments the count of votes for "op" by 1
        person_number += 1
        count_person += 1
    elif op == 0:
        break
    else:
        print("Invalid choice")
        continue

print("\nThe results are as follows:")
print("Total number of people participated:", count_person)
print("\nBeverage           Number of Votes")
print("*" * 40)

z = list(zip(votes, beverages))
z.sort(reverse=True)

for vote, bev in z:
    print(f"{bev:<18} {vote}")
