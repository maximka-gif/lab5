# Задання початкових даних
cost_price = 30   # собівартість товару
initial_price = 50 # початкова ціна товару
inventory = 1000   # кількість товарів на складі

# Вірогідності
p_hot_summer = 0.6
p_cold_summer = 0.4
p_theta1_given_xi1 = 0.7
p_theta2_given_xi1 = 0.3
p_theta1_given_xi2 = 0.4
p_theta2_given_xi2 = 0.6

# Варіанти зниження ціни та обсяги продажів за еластичностями
discounts = {
    0.2: {'theta1': 700, 'theta2': 400}, # зниження на 20%
    0.3: {'theta1': 800, 'theta2': 500}, # зниження на 30%
    0.4: {'theta1': 900, 'theta2': 600}  # зниження на 40%
}

# Функція для розрахунку збитків при вибраному варіанті зниження ціни
def calculate_loss(discount, demand_theta1, demand_theta2):
    sale_price = initial_price * (1 - discount)
    revenue_theta1 = sale_price * demand_theta1
    revenue_theta2 = sale_price * demand_theta2
    total_cost = cost_price * inventory
    loss_theta1 = total_cost - revenue_theta1
    loss_theta2 = total_cost - revenue_theta2
    return loss_theta1, loss_theta2

# Розрахунок очікуваних збитків для кожного варіанту зниження ціни
expected_losses = {}

for discount, demands in discounts.items():
    loss_theta1, loss_theta2 = calculate_loss(discount, demands['theta1'], demands['theta2'])
    
    # Обчислення очікуваних збитків
    expected_loss = (
        p_hot_summer * (p_theta1_given_xi1 * loss_theta1 + p_theta2_given_xi1 * loss_theta2) +
        p_cold_summer * (p_theta1_given_xi2 * loss_theta1 + p_theta2_given_xi2 * loss_theta2)
    )
    expected_losses[discount] = expected_loss

# Пошук варіанту з мінімальними збитками
optimal_discount = min(expected_losses, key=expected_losses.get)
minimal_loss = expected_losses[optimal_discount]

# Виведення результатів
print("Очікувані збитки для кожного варіанту зниження ціни:")
for discount, loss in expected_losses.items():
    print(f"Зниження ціни на {int(discount * 100)}%: Очікувані збитки = ${loss:.2f}")

print(f"\nРекомендоване зниження ціни для мінімальних збитків: {int(optimal_discount * 100)}% з очікуваними збитками ${minimal_loss:.2f}")
