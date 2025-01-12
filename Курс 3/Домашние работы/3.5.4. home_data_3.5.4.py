import numpy as np

def normalize(data):
    data_copy = data.copy()  # Создаем копию исходной матрицы

    min_vals = data_copy.min(axis=1, keepdims=True)  # Минимальные значения по строкам
    max_vals = data_copy.max(axis=1, keepdims=True)  # Максимальные значения по строкам

    # Нормализуем данные по строкам
    normalized_data = (data_copy - min_vals) / (max_vals - min_vals)
    normalized_data = np.round(normalized_data, 4)  # Округляем до 4 знаков после запятой

    return normalized_data
