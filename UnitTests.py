#Unit test for DumbHotEncoder

import DumbHotEncoder

def MonthsTest():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    encoder = DumbHotEncoder.DumbHotEncoder()
    encoder.fit(months)
    res = encoder.transform(['January'])
    print res

def MonthsTest2():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    encoder = DumbHotEncoder.DumbHotEncoder()
    res = encoder.fit_transform(months)
    print res

# MonthsTest()
MonthsTest2()