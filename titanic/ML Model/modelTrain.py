import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def lostValues(database):
        Age = database[0]
        Pclass = database[1]

        if pd.isnull(Age):
            if Pclass == 1:
                return 37
            elif Pclass == 2:
                return 29
            else:
                return 24
        else:
            return Age

def main():
    database = pd.read_csv("/home/foesa/Documents/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv")
    database['Age'] = database[['Age', 'Pclass']].apply(lostValues, axis=1)
    database.drop('Cabin', axis=1, inplace=True)
    sex = pd.get_dummies(database['Sex'], drop_first=True)
    embarked = pd.get_dummies(database['Embarked'], drop_first=True)
    database.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
    database.drop('PassengerId', axis=1, inplace=True)
    pd.concat([database, sex, embarked], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(database.drop('Survived', axis=1), database['Survived'],test_size=0.30, random_state=101)
    mainModel = LogisticRegression()
    mainModel.fit(X_train, y_train)
    filename = 'final_model.sav'
    pickle.dump(mainModel, open(filename, 'wb'))

if __name__ == '__main__':
    main()