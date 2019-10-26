import matplotlib.pyplot as plt


class ExploratoryDataAnalysis:

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def info(self):
        return self.data_frame.info()

    def describe(self):
        return self.data_frame.describe()

    def histogram(self):
        self.data_frame.hist(bins=50, figsize=(15, 10))
        plt.show()
