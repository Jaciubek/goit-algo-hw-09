def find_coins_greedy(amount):
    coins = [50, 20, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin
        
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 20, 50]
    max_amount = amount + 1
    # Initialize the dynamic programming table
    dp = [float('inf')] * max_amount
    dp[0] = 0
    coin_used = [{} for _ in range(max_amount)]
    
    for i in range(1, max_amount):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin_used[i - coin].copy()
                    if coin in coin_used[i]:
                        coin_used[i][coin] += 1
                    else:
                        coin_used[i][coin] = 1
    
    return coin_used[amount]

import time
def compare_performance(amount):

# Measure execution time of the greedy algorithm
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    end_time = time.time()
    greedy_time = end_time - start_time

# Measure execution time of the dynamic programming algorithm
    start_time = time.time()
    dp_result = find_min_coins(amount)
    end_time = time.time()
    dp_time = end_time - start_time

    print(f"Greedy Algorithm for amount {amount}: {greedy_result} (Time: {greedy_time:.6f} seconds)")
    print(f"Dynamic Programming for amount {amount}: {dp_result} (Time: {dp_time:.6f} seconds)")

    #print("Greedy Algorithm:", find_coins_greedy(amount))
    #print("Dynamic Programming:", find_min_coins(amount))

compare_performance(119)

# Result for really large amount
compare_performance(1995661)