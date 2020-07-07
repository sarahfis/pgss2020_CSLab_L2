# -*- coding: utf-8 -*-
"""LoadingIRISData

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gxKT5TZ-KaqFYxODYH8QAJFNoIibm9Hs

# Load Data
"""

from sklearn.datasets import load_iris
iris = load_iris()

"""# Structure the Data into a Data Frame
- Import pandas to be used as "pd."
- Print the frame
- by columns
"""

import pandas as pd
X = pd.DataFrame(data = iris.data, columns = iris.feature_names)
#features are columns
#python lists start at 0, R starts at 1
print(X.head())

"""#Create a Second Data Frame
- by rows
"""

y = pd.DataFrame(data=iris.target, columns = ['irisType'])
y.head()

"""# Descriptive Analysis on the Data Frame
- Creating a Frequency Table
"""

y.irisType.value_counts()



"""# Create and structure a different type of data frame"""

y = pd.DataFrame(data=iris.target, columns = ['irisType'])
y.head()

#rows are records columns are attributes
#address each column seperately (first as 0)
# : is all 
# rows, columns -> so :,0 is ALL of the rows for the first column; :,1 second; :,2 third; etc.
import pandas as pd
data=pd.DataFrame({
    'SepalLength':iris.data[:,0],
    'SepalWidth':iris.data[:,1],
    'PetalLength':iris.data[:,2],
    'PetalWidth':iris.data[:,3],
    'Species':iris.target
})
data.head()

"""# Descriptive Analysis on that data frame"""

y.irisType.value_counts()

data['Species'].value_counts()