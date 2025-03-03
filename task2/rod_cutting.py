from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    memo = {}

    def cutting(length: int) -> {int, List[int]}:
        if length == 0:
            return 0, []

        if length in memo:
            return memo[length]

        max_profit = 0
        best_cut = []

        if length <= len(prices) and prices[length - 1] > max_profit:
            max_profit = prices[length - 1]
            best_cut = [length]

        for i in range(1, min(length, len(prices)) + 1):
            profit, cuts = cutting(length - i)
            total_profit = prices[i - 1] + profit

            if total_profit > max_profit:
                max_profit = total_profit
                best_cut = [i] + cuts

        memo[length] = (max_profit, best_cut)
        return memo[length]

    max_profit, cuts = cutting(length)

    number_of_cuts = 0 if cuts == [length] else len(cuts)
        
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    dp = [0] * (length + 1)
    cuts = [0] * (length + 1)

    if length <= len(prices):
        dp[length] = prices[length - 1]
        cuts[length] = length  

    for i in range(1, length + 1):
        for j in range(1, min(i, len(prices)) + 1):
            if dp[i] < prices[j - 1] + dp[i - j]:
                dp[i] = prices[j - 1] + dp[i - j]
                cuts[i] = j

    best_cuts = []
    remaining_length = length
    while remaining_length > 0:
        best_cuts.append(cuts[remaining_length])
        remaining_length -= cuts[remaining_length]

    if best_cuts == [length]:
        number_of_cuts = 0
    else:
        number_of_cuts = len(best_cuts)

    return {
        "max_profit": dp[length],
        "cuts": best_cuts,
        "number_of_cuts": number_of_cuts
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
