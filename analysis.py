import matplotlib.pyplot as plt


class ExploratoryDataAnalysis:
    attributes = []

    def __init__(self, data_frame):
        self.data_frame = data_frame
        [self.attributes.append(attr) for attr in data_frame]

        for attr in self.attributes:
            if self.data_frame.dtypes[attr] == 'object':
                print('Looks like there is a categorical attribute: {categorical_attribute}'.format(categorical_attribute=attr))
                user_input = input('Would you like to perform a count on this attribute? [y/n]: ')
                if user_input == 'y':
                    print(self.value_count(attr))

    def info(self):
        return self.data_frame.info()

    def describe(self):
        return self.data_frame.describe()

    def histogram(self):
        self.data_frame.hist(bins=50, figsize=(15, 10))
        plt.show()

    def value_count(self, attribute: list):
        return self.data_frame[attribute].value_counts()
