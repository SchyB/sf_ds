import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, потом уменьшаем
    или увеличиваем в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    mn = 1 #границы для предполагаемого числа
    mx = 101
    count = 0 #число попыток
    predict = np.random.randint(mn, mx) #предполагаемое число

    while number != predict:
        count += 1
        if predict > number:
            mx = predict - 1
            predict = round((mx+mn) // 2) #сужаем границы
        elif predict < number:
            mn = predict + 1
            predict = round((mx+mn) // 2)

    return count

def score_game(game_core_v3) -> int: 
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """ 
    count_ls = []  #список для сохранения количества попыток
    np.random.seed(1) #фиксируется сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) #находим среднее количество попыток

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    return score
score_game(game_core_v3)