import numpy as np 
import pandas as pd
import operator
import matplotlib.pyplot as plt

data = pd.read_csv('presidents.csv')
df = pd.DataFrame(data, columns = ['BIRTH DATE', 'DEATH DATE'])

date_of_birth = df["BIRTH DATE"].values.tolist()
date_of_death = [y if type(y) == str else '9999' for y in df["DEATH DATE"].values.tolist()]

df = [[x[-4:], y[-4:]] for x, y in zip(date_of_birth, date_of_death)]
def num_alive_presidents(year):
    """returns the number of presidents alive at that year"""
    return sum(1 if (int(x[0][-4:]) <= year and (year <= int(x[1][-4:]) or x[1] == 'nan')) else 0 for x in df)


def most_alive_year():
    """returns the years where the most presidents were alive during that year"""
    year_dict = {x: num_alive_presidents(x) for x in range(1732,2017)}
    max_alive = max(year_dict.values())
    
    return [x for x in year_dict if year_dict[x] == max_alive]

print most_alive_year()