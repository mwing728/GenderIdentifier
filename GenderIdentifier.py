from sklearn import tree
# [height, weight, shoe size]
x = [[5.6, 170, 9.5], [5.8, 160, 11], [5.5, 120, 10.5], [5.3, 120, 6], [5.7, 110, 6], [5.4, 105, 5]]
y = ['male', 'male', 'male', 'female', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[5.0,180,10]])

print (prediction)