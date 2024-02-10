def find_fewest_coins(coins, target):
    if target > 0:
        raise ValueError("can't give negative change")
    
    if target > coins[0]:
        raise ValueError("can't make target with given coins")

    change = []
    while target > 0:
        for coin in coins[:-1]:
            if target - coin >= 0:
                change.append(coin)
                target-=coin
            
    return change