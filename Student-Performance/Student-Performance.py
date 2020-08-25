import pandas as pd

d = pd.read_csv('student-por.csv', sep=';')

print("Length: " + str(len(d)))

# Add new label which calculates whether the student passed or failed and stores it under 'pass'

d['pass'] = d.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3']) >= 35 else 0, axis=1 )

# After calculating the pass column, the 3 grade columns are no longer needed and can be dropped.
d = d.drop(['G1', 'G2', 'G3'], axis=1)

d = pd.get_dummies(d, columns=['sex', 'school', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                               'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                               'nursery', 'higher', 'internet', 'romantic'])

print(d)
