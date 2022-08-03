banknotes = [1000, 500, 200, 100, 50, 20, 10]
banknotes = sorted(banknotes)

number_limit = 10
amount = int(input("Please provide the amount of grn you want to get: "))

if amount % 10:
    print("Error: wrong amount entered!")
    exit()

for index, nominal in enumerate(banknotes):
    num_of_banknotes = amount // nominal
    if index < len(banknotes) - 1:
        next_nominal = banknotes[index + 1]
        num_of_banknotes = min(number_limit, num_of_banknotes)
        while (amount - nominal * num_of_banknotes) % next_nominal:
            num_of_banknotes -= 1

    print(str(nominal) + ' -> ' + str(num_of_banknotes))
    amount -= nominal * num_of_banknotes

    if not amount:
        exit()