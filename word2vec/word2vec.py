from gensim.models import word2vec
from gensim.models.word2vec import Word2Vec
import multiprocessing

sentences = word2vec.Text8Corpus('new_dict.txt') 
model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=multiprocessing.cpu_count())  # 生成词向量
model.save('Word2VecModel.model') 
model.wv.save_word2vec_format('Word2VecModel.vector', binary=False)
