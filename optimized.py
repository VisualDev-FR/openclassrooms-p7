import typing
import time

MAX_BUDGET_PER_CLIENT = 500

class Action:
    """
    Simple class container for actions datas
    """
    def __init__(self, name: str, cost: float, benefit_rate: float) -> None:
        self.name = name
        self.cost = cost
        self.benefit_rate = benefit_rate
        self.benefit = self.cost * benefit_rate / 100

    def __repr__(self) -> str:
        return f"{self.name} {self.cost:.02f} {self.benefit:.02f}"


def read_data() -> typing.List[Action]:
    """
    read and parse the datas contained in bruteforce_data.csv to a list of Actions
    """

    result = []
    
    # file =  "data/dataset1_Python+P7.csv"
    file =  "data/dataset2_Python+P7.csv"
    # file = "bruteforce_data.csv"

    # read the csv file as a list
    with open(file, "r") as reader:
        datas = reader.readlines()[1:]

    for data in datas:

        # split one csv line and ignore the last character ('\n')
        action_name, action_cost, action_benefit = data[:-1].split(",")

        # create a new Action object
        action = Action(
            name=action_name,
            cost=float(action_cost),
            benefit_rate=float(action_benefit)
        )

        # append the new Action in the results list
        result.append(action)

    return result


def knapsack_real_values(weights, values, max_weight):
    n = len(weights)
    constant = 100  # Utiliser une constante pour multiplier les valeurs réelles
    weights = [int(w * constant) for w in weights]
    values = [int(v * constant) for v in values]
    max_weight = int(max_weight * constant)

    print(max_weight, n, max_weight * n)

    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for row in range(1, n + 1):
        for w in range(max_weight + 1):

            # print(f"\r{row}, {w}", end="")

            if weights[row - 1] <= w:
                dp[row][w] = max(
                    dp[row - 1][w],
                    dp[row - 1][w - weights[row - 1]] + values[row - 1]
                )
            else:
                dp[row][w] = dp[row - 1][w]

    # Reconstruction de la solution
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    max_value = sum(values[i] for i in selected_items) / constant  # Diviser par la constante pour obtenir la valeur réelle
    return max_value, selected_items


actions = read_data()

weights = [action.cost for action in actions if action.cost > 0]
values = [action.benefit for action in actions if action.cost > 0]
max_weight = 500
max_value, selected_items = knapsack_real_values(weights, values, max_weight)
print("Valeur maximale obtenue:", max_value)
print("Éléments sélectionnés:", selected_items)

