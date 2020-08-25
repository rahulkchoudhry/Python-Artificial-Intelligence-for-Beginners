import pandas as pd
import numpy as np

d = pd.read_csv('student-por.csv', sep=';')

print("Length: " + str(len(d)))

# Add new label which calculates whether the student passed or failed and stores it under 'pass'
d['pass'] = d.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3']) >= 35 else 0, axis=1)

# After calculating the pass column, the 3 grade columns are no longer needed and can be dropped.
d = d.drop(['G1', 'G2', 'G3'], axis=1)

# Convert all data to numerical data
d = pd.get_dummies(d, columns=['sex', 'school', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                               'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                               'nursery', 'higher', 'internet', 'romantic'])

# Shuffle data
d = d.sample(frac=1)

# Split data into train and test data
d_train = d[:500]
d_test = d[500:]

# split up the data into attributes and pass result for test, train and all
d_train_att = d_train.drop(['pass'], axis=1)
d_train_pass = d_train['pass']

d_test_att = d_test.drop(['pass'], axis=1)
d_test_pass = d_test['pass']

d_att = d.drop(['pass'], axis=1)
d_pass = d['pass']

# calculate number of passing students in the data set
print("Passing: %d out of %d (%.2f%%)" % (np.sum(d_pass), len(d_pass), 100*float(np.sum(d_pass))/len(d_pass)))

print(d)
