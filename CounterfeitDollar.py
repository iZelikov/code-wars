def is_counterfeit(coin, weight, results):
    coin_is_counterfeit = True
    for result in results:
        left, right, ballance = result.split(" ")
        if weight == "heavy":
            match ballance:
                case "even":
                    coin_is_counterfeit &= coin not in left and coin not in right
                case "up":
                    coin_is_counterfeit &= coin in left and coin not in right
                case "down":
                    coin_is_counterfeit &= coin not in left and coin in right
        elif weight == "light":
            match ballance:
                case "even":
                    coin_is_counterfeit &= coin not in left and coin not in right
                case "up":
                    coin_is_counterfeit &= coin not in left and coin in right
                case "down":
                    coin_is_counterfeit &= coin in left and coin not in right
        else:
            return False
    return weight if coin_is_counterfeit else False


def counterfeit_dollar(results):
    coins = "ABCDEFGHIJKL"
    output = []
    for coin in coins:
        if is_counterfeit(coin, "light", results):
            output.append((coin,"light"))
        if is_counterfeit(coin, "heavy", results):
            output.append((coin,"heavy"))
    if len(output) == 1:
        return f'{output[0][0]} is the counterfeit coin and it is {output[0][1]}.'
    else:
        return "???"

results = ['ABCD EFGH even',
      'ABCI EFJK up',
      'ABIJ EFGH even']

counterfeit_dollar(results)
