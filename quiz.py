import pandas as pd
import numpy as np
from scipy.stats import pearsonr, kurtosis, skew



url = 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
ferc = pd.read_csv(url, error_bad_lines=False)

#calculating sum of null values and percentage of null values in fuel_unit column
nul_val = ferc['fuel_unit'].isnull().sum()
perc = (nul_val*100)/ferc['fuel_unit'].count()
print('Feature: fuel_unit, Total: {}, Percent: {:.3f}'.format(nul_val, perc))

#kurtosis and skewness for quantity of fuel burned
print("Kurtosis: {:.2f}, Skewness: {:.2f}".format(kurtosis(ferc['fuel_qty_burned']), skew(ferc['fuel_qty_burned']))

#average fuel cost per unit delivered by year
ferc.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()

int_col = ferc.describe().columns
for data in int_col:
      print("Correlation: ", pearsonr(ferc['fuel_cost_per_unit_burned'], ferc[data]))

      
