from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns1(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    
# All sklearn Transforms must have the `transform` and `fit` methods
class Duplicar(BaseEstimator, TransformerMixin):
    def __init__(self, nombre):
        self.nombre = nombre

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data[self.nombre] = data[self.nombre] * 2
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data
