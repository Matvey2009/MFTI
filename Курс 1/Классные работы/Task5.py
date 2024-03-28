import pandas as pd

def best_of(data: pd.DataFrame, target: str):
	f_df = data[(data['Группа'] == target) & (data['Оценка'] >= 75)]['Фамилия']
	return list(f_df)
