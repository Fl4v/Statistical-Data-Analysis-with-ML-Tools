from preprocessing import data
from analysis import ExploratoryDataAnalysis

Analysis = ExploratoryDataAnalysis(data('q1_q16_stellar_clean.csv'))

Analysis.info()
