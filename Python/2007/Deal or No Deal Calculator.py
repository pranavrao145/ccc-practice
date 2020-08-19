# J3 

briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

totalsum = 0
terms = 0

done = int(input("Enter the amount of cases that have been picked: "))

if done == 10:
    print('No Deal')
    exit()
elif done < 1 or done > 10:
    print("That is not a valid input. Please try again.")
    exit()

for i in range(done):
    x = (int(input("Enter a case number that was taken out: "))) - 1
    if x < 0 or x > 10:
        print("That is not a valid input. Please try again.")
        exit()
    else:
        briefcases[x] = 0

offer = int(input("Enter the banker's offer: "))

for i in briefcases:
    if i == 0:
        continue
    else:
        totalsum += i
        terms += 1

avg = totalsum/terms

if offer > avg:
    print("Deal")
else:
    print("No Deal")
