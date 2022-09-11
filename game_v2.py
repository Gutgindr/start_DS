#Компьютер сам загадывает и отгадывает числа

import numpy as np

def random_predict(number:int=1) -> int:
    """Принимает на вход число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number: 
            break
    return(count)
print(f"Количество попыток: {random_predict()}")

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Лист для количества попыток
    np.random.seed(0)
    random_array = np.random.randint(1,101, size=(10))

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)

score_game(random_predict)