import heapq


def min_cost_to_connect_cables(cable_lengths):
    # Створення мінімальної купи з довжин кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0
    # Поки в купі більше одного елемента
    while len(cable_lengths) > 1:
        # Видаляємо два найменших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Обчислюємо витрати на їх з'єднання
        cost = first + second
        total_cost += cost

        # Вставляємо новоутворений кабель назад до купи
        heapq.heappush(cable_lengths, cost)

    return total_cost


print(
    f'Мінімальна сума загальних витрат: {min_cost_to_connect_cables([8, 4, 6, 12])}')
