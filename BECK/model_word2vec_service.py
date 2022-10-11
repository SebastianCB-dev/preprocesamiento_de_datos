from pprint import pprint
from gensim.models import Word2Vec
import numpy as np

class ModelWord2Vec:

  def __init__(self):
    """
    La función toma una lista de palabras y devuelve una lista de vectores.
    """
    self.model = Word2Vec.load('word2vec.model')

  def get_model(self):
    """
    me devuelve el modelo
    :return: El modelo está siendo devuelto.
    """
    return self.model
  
  def add_corpus(self, corpus):
    """
    > La función toma un corpus (una lista de palabras) y lo agrega al modelo
    
    :param corpus: El corpus es una lista de listas. Cada lista es un documento. Cada documento es una
    lista de palabras
    """
    corpus = [corpus]
    self.model.build_vocab(corpus, update=True)
    self.save_model()

  def save_model(self):
    """
    Esta funcion guarda el modelo
    """
    self.model.save('word2vec.model')

  def get_euclidian_distance(self, corpus_a, corpus_b):
    """
    Si la longitud de las dos listas no es igual, agregue ceros a la lista más corta hasta que sean
    iguales. Luego, devuelva la distancia euclidiana entre las dos listas.
    
    :param corpus_a: El primer corpus a comparar
    :param corpus_b: El segundo corpus a comparar
    :return: La distancia euclidiana entre dos vectores.
    """
    vector_corpus_a = self.get_word_vector(corpus_a)
    vector_corpus_a = list(np.array(vector_corpus_a).tolist())
    vector_corpus_b = self.get_word_vector(corpus_b)
    vector_corpus_b = list(np.array(vector_corpus_b).tolist())
    #Diferencia entre ambos
    if len(vector_corpus_a) != len( vector_corpus_b):
      diferencia = abs(len(vector_corpus_a) - len( vector_corpus_b)) 
      if len(vector_corpus_a) > len( vector_corpus_b):
            i = 0
            while i < diferencia:
              vector_corpus_b.append(self.getVector250())
              i += 1
            return np.linalg.norm(np.array(vector_corpus_a) - np.array(vector_corpus_b))
      if len(vector_corpus_a) < len(vector_corpus_b):
            i = 0
            while i < diferencia:
              vector_corpus_a.append(self.getVector250())
              i += 1
            return np.linalg.norm(np.array(vector_corpus_a) - np.array(vector_corpus_b))
    else:
      return np.linalg.norm(np.array(vector_corpus_a) - np.array(vector_corpus_b))


  def get_cosine_distance(self, corpus_a, corpus_b):
    """
    La función toma dos cadenas como entrada y devuelve la distancia del coseno entre las dos cadenas.
    
    :param corpus_a: El primer corpus a comparar
    :param corpus_b: El corpus para comparar con el corpus_a corpus
    :return: La distancia del coseno entre los dos corpus.
    """
    return self.model.wv.wmdistance(corpus_a, corpus_b)

  def get_word_vector(self, word):
    """
    > La función toma una palabra como entrada y devuelve el vector de palabra para esa palabra
    
    :param word: La palabra cuya representación vectorial desea obtener
    :return: La palabra vector para la palabra.
    """
    return self.model.wv[word]

  def getVectorBeck(self, commentVector, beck):
    array = []
    for item in beck.keys():
      for idx, result in enumerate(beck[item].keys()): 
        if idx == 0:
          itemBeck = beck[item][result]
        if( self.get_cosine_distance(commentVector, itemBeck["data"]) < 
        self.get_cosine_distance(commentVector, beck[item][result]["data"])):
          itemBeck = beck[item][result]
      array.append(itemBeck['value'])   
    return array

  def getVector250(self):
    return list(np.zeros(250))

    
    
    