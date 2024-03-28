import pandas as pd
import numpy as np
def count_nan(data: pd.DataFrame):
	return data.isnull().sum().sum()
