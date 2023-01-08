# %%
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
import joblib

# %%
data = load_breast_cancer()
x = data['data']
y = data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
clf = KNN()
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
filename = 'breast_cancer_detection_model.sav'
joblib.dump(clf, filename)
# loaded = joblib.load(filename)
# print(loaded.score(x_test, y_test))


