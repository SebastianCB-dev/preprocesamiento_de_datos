## Preprocesamiento de datos
Este es un repositorio dedicado al preprocesamiento de datos en Python usando diferentes librerías.

Lo que se hace:
* stop words removal
* emoji removal
* punctuaction sign removal
* Hashtags and mentions removal
* Lemmatization
* Normalization

# Módulos
* emoji 
* nltk
* sklearn
* spacy 
* stanza
* wheel
* hunspell
* numpy
* gensim
* pyemd
* joblib
* skicit-learn
```
pip install emoji nltk sklearn spacy stanza wheel hunspell numpy gensim pyemd joblib scikit-learn
```
o
```
pip3 install emoji nltk sklearn spacy stanza wheel hunspell numpy gensim pyemd joblib scikit-learn
```

# Errores:
1. Error al instalar hunspell:
   - Se solventa instalando libhunspell-dev (Ubuntu)
  
  ```
  sudo apt-get install libhunspell-dev
  ```
2. Error con modelo 'es_core_news_md' de Spacy:
   - Se solventa descargandolo:

  ```
  python -m spacy download es_core_news_md
  python3 -m spacy download es_core_news_md
  ```
## Data
Para entrenar mas corpus al modelo
```
model.build_vocab(data)
```

Para cargar el modelo
```
Word2Vec.load('word2vec.model')
```

Para guardar el modelo
```
model.save('word2vec.model')
```

Para distancia de coseno entre dos textos convertidos a arreglos.
```
coseno = model.wv.wmdistance(first_array, second_array)
```

## Citations
Ofir Pele and Michael Werman "A linear time histogram metric for improved SIFT matching" &lt;http://www.cs.huji.ac.il/\~werman/Papers/ECCV2008.pdf&gt;_

Ofir Pele and Michael Werman "Fast and robust earth mover's distances" &lt;https://ieeexplore.ieee.org/document/5459199/&gt;_

Matt Kusner et al. "From Word Embeddings To Document Distances" &lt;http://proceedings.mlr.press/v37/kusnerb15.pdf&gt;

#### **Model:** 

https://zenodo.org/record/1410403#.Y1fknbbMJD8

Aitor Almeida, & Aritz Bilbao. (2018). Spanish 3B words Word2Vec Embeddings (Version 1.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1410403

Bilbao-Jayo, A., & Almeida, A. (2018). Automatic political discourse analysis with multi-scale convolutional neural networks and contextual data. International Journal of Distributed Sensor Networks, 14(11), 1550147718811827.
