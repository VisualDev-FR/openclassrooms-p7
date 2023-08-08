import time
import action


def knapsack_solver(weights, values, max_weight):

    # muliply all values to get integers instead of float
    constant = 100
    weights = [int(w * constant) for w in weights]
    values = [int(v * constant) for v in values]
    max_weight = int(max_weight * constant)

    # initialize the dynamic programming matrix
    n = len(weights)
    matrix = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # find the optimal solution
    for row in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[row - 1] <= w:
                matrix[row][w] = max(
                    matrix[row - 1][w],
                    matrix[row - 1][w - weights[row - 1]] + values[row - 1]
                )
            else:
                matrix[row][w] = matrix[row - 1][w]

    # retreive the selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if matrix[i][w] != matrix[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    # divide the obtained result by constant to get the real max value
    max_value = matrix[n][max_weight] / constant
    total_cost = sum(weights[i] for i in selected_items) / constant

    return max_value, total_cost, selected_items


if __name__ == "__main__":
    
    start = time.time()

    # read input datas
    actions = [action for action in action.read_bruteforce_data() if action.cost > 0]

    # filter the actions with positive cost
    weights = [action.cost for action in actions]
    values = [action.benefit for action in actions]

    # solve the optimal solution
    max_benefit, total_cost, items = knapsack_solver(weights, values, action.MAX_BUDGET_PER_CLIENT)

    print("\n" + "-" * 50)
    print(f"max_benefit = {max_benefit}, total_cost = {total_cost}, timer = {time.time() - start:.02f}s, items :")

    for index in items:
        print(actions[index].name, actions[index].cost, sep=",")
