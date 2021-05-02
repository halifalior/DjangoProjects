from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model


#global variables

target = pd.DataFrame()
predictors = pd.DataFrame()
tree_filename = 'c:\\users\\user\\titanic_tree.sav'
knn_filename='c:\\users\\user\\titanic_knn.sav'
lr_filename='c:\\users\\user\\titanic_lr.sav'


def prepare_data_for_classification():
    df = pd.read_csv("C:\\Users\\user\\Downloads\\titanic\\train.csv")

    def get_title(name):
        if '.' in name:
            return name.split(',')[1].split('.')[0].strip()
        else:
            return 'Unknown'

    # A list with the all the different titles
    titles = sorted(set([x for x in df.Name.map(lambda x: get_title(x))]))

    # Normalize the titles
    def replace_titles(x):
        title = x['Title']
        if title in ['Capt', 'Col', 'Major']:
            return 'Officer'
        elif title in ["Jonkheer", "Don", 'the Countess', 'Dona', 'Lady', "Sir"]:
            return 'Royalty'
        elif title in ['the Countess', 'Mme', 'Lady']:
            return 'Mrs'
        elif title in ['Mlle', 'Ms']:
            return 'Miss'
        else:
            return title

    # Lets create a new column for the titles
    df['Title'] = df['Name'].map(lambda x: get_title(x))

    # And replace the titles, so the are normalized to 'Mr', 'Miss' and 'Mrs'
    df['Title'] = df.apply(replace_titles, axis=1)

    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    df['Embarked'].fillna("S", inplace=True)
    df.drop("Cabin", axis=1, inplace=True)
    df.drop("Ticket", axis=1, inplace=True)
    df.drop("Name", axis=1, inplace=True)
    df.Sex.replace(('male', 'female'), (0, 1), inplace=True)
    df.Embarked.replace(('S', 'C', 'Q'), (0, 1, 2), inplace=True)
    df.Title.replace(('Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Officer', 'Royalty'), (0, 1, 2, 3, 4, 5, 6, 7),
                     inplace=True)

    predictors = df.drop(['Survived', 'PassengerId'], axis=1)
    target = df["Survived"]
    return predictors, target

def prepare_data_for_linear_regression():
    df1 = pd.read_csv("C:\\Users\\user\\Downloads\\titanic\\train1.csv")
    x = df1[['Age', 'Sex', 'SibSp', 'Title', 'Embarked']]
    y = df1.Price
    lm = linear_model.LinearRegression()
    model = lm.fit(x, y)
    # save the tree model
    pickle.dump(model, open(lr_filename, 'wb'))
    # return accuracy
    return lm.score(x,y)

def predict_by_linear_regression( Age, Sex, SibSp, Title, Embarked):
    x = [[Age, Sex, SibSp, Title, Embarked]]
    model = pickle.load(open(lr_filename, 'rb'))
    prediction = model.predict(x)
    return (prediction[0])

def tree_model(predictors, target):
    x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.30, random_state=0)
    features = predictors.columns

    clf = DecisionTreeClassifier(criterion="gini", max_depth=5)
    clf = clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    # save the tree model
    pickle.dump(clf, open(tree_filename, 'wb'))

    # return accuracy
    return metrics.accuracy_score(y_test, y_pred)

def print_tree(predictors):
    # load the tree model
    clf = pickle.load(open(tree_filename, 'rb'))
    # print the tree
    features = predictors.columns
    plt.figure(figsize=[13, 13])
    plot_tree(clf, feature_names=features, class_names=['survived', 'not survived'], filled=True)
    plt.show()

def predict_by_tree(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title):
    x=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    clf = pickle.load(open(tree_filename, 'rb'))
    prediction=clf.predict(x)
    return (prediction[0])


def knn_model(predictors, target):
    x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.30, random_state=0)
    features = predictors.columns

    def find_best_k():
        k_range = range(3, 21)
        scores = {}
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(x_train, y_train)
            y_pred = knn.predict(x_test)
            scores[k] = metrics.accuracy_score(y_test, y_pred)

        # find the k for the max score - option 1

        return (max(scores, key=scores.get))

    print(find_best_k())

    knn = KNeighborsClassifier(n_neighbors=find_best_k())
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)

    # save the tree model
    pickle.dump(knn, open(knn_filename, 'wb'))

    # return accuracy
    return metrics.accuracy_score(y_test, y_pred)

def predict_by_knn(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title):
    x = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title]]
    knn = pickle.load(open(knn_filename, 'rb'))
    prediction = knn.predict(x)
    return (prediction[0])


