def knapsack_real_values(weights, values, max_weight):
    n = len(weights)
    constant = 1000  # Utiliser une constante pour multiplier les valeurs réelles
    weights = [int(w * constant) for w in weights]
    values = [int(v * constant) for v in values]
    max_weight = int(max_weight * constant)

    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruction de la solution
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    max_value = sum(values[i] for i in selected_items) / constant  # Diviser par la constante pour obtenir la valeur réelle
    return max_value, selected_items

weights = [2.1, 3.5, 4.8, 5.0]
values = [3.7, 5.2, 7.8, 8.1]
max_weight = 8
max_value, selected_items = knapsack_real_values(weights, values, max_weight)
print("Valeur maximale obtenue:", max_value)
print("Éléments sélectionnés:", selected_items)
