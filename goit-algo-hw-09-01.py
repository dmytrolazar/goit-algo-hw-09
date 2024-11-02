
def find_coins_greedy(change_amount: int):
    change_dict = {}
    if change_amount < 1:
        print("Enter a positive amount.")
    else:
        for coin in coins:
            if change_amount >= coin:
                change_dict[coin] = change_amount // coin
                change_amount = change_amount % coin
                if change_amount == 0:
                    break
    return change_dict

def find_min_coins(change_amount: int):
    if change_amount < 1:
        print("Enter a positive amount.")

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [(0, {})] # кортеж з загальної кількості необхідних монет і словника необхідних монет
    
    # будуємо таблицю K знизу вгору, від 1 монети до
    for amount in range(1, change_amount + 1):
        # для кожної монети, яка менша за значення, яке ми обраховуємо, шукаємо в таблиці K раніше обраховане значення на позиції залишку після використання цієї монети. Тоді вибираємо те, що потребує найменшої кількості монет і додаємо до нього цю монету
        coin, coin_number, coin_dict = min([(coin, K[amount - coin][0],K[amount - coin][1].copy()) for coin in list(filter(lambda c: c <= amount, coins))], key=lambda x:x[1])
        coin_dict[coin] = coin_dict.get(coin, 0) + 1
        K.append((coin_number + 1, coin_dict))
        #print(amount, K)

    return K[change_amount][1]

coins = [50, 25, 10, 5, 2, 1]
print(find_coins_greedy(0))
print(find_min_coins(0))
print(find_coins_greedy(113))
print(find_min_coins(113))
print(find_coins_greedy(1234))
print(find_min_coins(1234))

coins = [25, 20, 1]
print(find_coins_greedy(80))
print(find_min_coins(80))
