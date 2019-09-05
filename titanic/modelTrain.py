import pandas as pd

class modelMaker ():
    def __init__(self,database):
        self.database = database

    def dataPrep(self):
        self.database['Age']= self.database[['Age','Pclass']].apply(self.lostValues, axis=1)
        self.database.drop('Cabin',axis=1,inplace=True)
        sex = pd.get_dummies(self.database['Sex'],drop_first=True)
        embarked = pd.get_dummies(self.database['Embarked'],drop_first=True)
        self.database.drop(['Sex','Embarked','Name','Ticket'],axis=1, inplace=True)
        self.database.drop('PasssengerId',axis=1,inplace=True)
        pd.concat([self.database,sex,embarked],axis=1)
        self.database.head()

    def lostValues(self):
        Age = self.database[0]
        Pclass = self.database[1]

        if pd.isnull(Age):
            if Pclass == 1:
                return 37
            elif Pclass == 2:
                return 29
            else:
                return 24
        else:
            return Age

    def trainModel(self):
        X = self.database.drop('Survived',axis=1)
        y = self.database['Survived']
