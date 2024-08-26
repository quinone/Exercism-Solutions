def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("can't give negative change")
    
    if target == 0:
        return []
    
    if target < coins[0]:
        raise ValueError("can't make target with given coins")

    change = []

    for coin in reversed(coins):
        while True:
            if coins[0] % 2 == 0:
                if target - coin >= 0 and target % coins[0] == 0:
                    change.append(coin)
                    target-=coin
                    break
            if target - coin > 0:
                change.append(coin)
                target-=coin
            if target - coin == 0:
                change.append(coin)
                target-=coin
                break
            if coin > target:
                break
        
    #for coin in reversed(coins):
    #    while coin <= target:
    #        if target - coin >= 0:
    #            change.append(coin)
    #            target-=coin
            
    return sorted(change)