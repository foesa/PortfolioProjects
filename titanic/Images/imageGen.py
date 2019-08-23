import pandas as pd
import numpy as np
import matplotlib.pyplot as matplot
import seaborn as sns

class imageMake():
    def __init__(self,path,database):
        self.path = path
        self.database = pd.read_csv(self.path)

    def imageCreate(self):
        sns.set_style('whitegrid')
        sexSaved = sns.countplot(x='Survived', hue='Sex', data=self.database, palette='RdBu_r')
        sexSaved.figure.savefig("sexSaved.png")

        matplot.clf()
        classSaved = sns.countplot(x='Survived', hue='Pclass', data=self.database)
        classSaved.figure.savefig("classSaved.png")

        matplot.clf()
        ageHist = self.database['Age'].plot.hist()
        ageHist.figure.savefig("ageHist.png")

        matplot.clf()
        agePlot = sns.boxplot(x='Pclass', y='Age', data=self.database)
        agePlot.figure.savefig("agePlot.png")

        matplot.clf()
        farePlot = sns.boxplot(x='Pclass',y='Fare', data=self.database)
        farePlot.figure.savefig("farePlot.png")

def main():
    images = imageMake("/home/foesa/Documents/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv",None)
    images.imageCreate()
if __name__ == '__main__':
    main()