from preprocessing import data
from analysis import ExploratoryDataAnalysis

analysis = ExploratoryDataAnalysis(data('q1_q16_stellar_clean.csv'))

print(analysis.describe())
print(analysis.correlation())
analysis.corr_matrix()
