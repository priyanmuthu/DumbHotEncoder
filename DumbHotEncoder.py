from collections import Iterable
class DumbHotEncoder:
    def __init__(self):
        self.valueSet = set()
        self.valueDict = {}
    
    def fit(self, X):
        # Create a set of values
        for v in X:
            self.valueSet.add(v)
        
        # Create a dictionary that can help transformation
        counter = 0
        for val in self.valueSet:
            self.valueDict[val] = counter
            counter += 1
    
    def transform(self, X):
        if(not isinstance(X, Iterable)):
            raise Exception('X not iterable, please pass an iterable parameter')
        result = []
        try:
            for x in X:
                onehot = [0]*len(self.valueSet)
                onehot[self.valueDict[x]] = 1
                result.append(onehot)
            return result
        except KeyError:
            raise Exception('KeyError: Incorrect value provided. Unable to transform')
        return None
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)