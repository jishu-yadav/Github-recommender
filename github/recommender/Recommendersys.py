import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Repository
import gensim
from gensim.parsing.preprocessing import preprocess_documents

df=pd.DataFrame((list(Repository.objects.all().values())))
def fit(keywords):
  df['description'].fillna('').astype(str)
  df['content']=df['content'].map(str)

  text_corpus = df['content'].values

  processed_corpus = preprocess_documents(text_corpus)
  dictionary = gensim.corpora.Dictionary(processed_corpus)
  bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

  tfidf = gensim.models.TfidfModel(bow_corpus)
  corpus_tfidf = tfidf[bow_corpus]

  lsi = gensim.models.LsiModel(corpus_tfidf, num_topics=200)
  index = gensim.similarities.MatrixSimilarity(lsi[corpus_tfidf])
  #cv = CountVectorizer()

  #count_matrix = cv.fit_transform(keywords)

  # print(count_matrix.toarray())

  #cosine_sim = cosine_similarity(count_matrix) 
  #return cosine_sim
  return dictionary,tfidf,index,lsi

def get_name_from_index(index):
		return df[df['id'] == index]["full_name"].values[0]

def get_index_from_owner(project_desc):
  #print(project_desc)
  #print(df.head())
  #print(df.loc(0)['id'])
  #cv=CountVectorizer
  return df[df.topics == project_desc]['id'].values[0]

def recommendations(dictionary,tfidf,index,lsi,desc):
  new_doc=gensim.parsing.preprocessing.preprocess_string(desc)
  new_vec = dictionary.doc2bow(new_doc)
  vec_bow_tfidf = tfidf[new_vec]
  vec_lsi = lsi[vec_bow_tfidf]

  sims = index[vec_lsi]

  for s in sorted(enumerate(sims), key=lambda item: -item[1])[:10]:
    print(df["full_name"].iloc[s[0]] , {str(s[1])})
  """contributor_index = get_index_from_owner(desc)
  #print(desc)
  print(contributor_index)
  #print(df.head())

  similar_project =  list(enumerate(cosine_sim[contributor_index]))

  sorted_similar_project = sorted(similar_project, key=lambda x:x[1], reverse=True)

  # top 15

  #print("\nPROJECT DESCRIPTION:\n" , df[df['index'] == sorted_similar_project[0][0]]["combined_features"].values[0] , "\n")
  #print("RECOMMENDED REPOSITORIES:-\n")

  i=0
  repo_list=[]
  for element in sorted_similar_project:
      name = get_name_from_index(element[0])
      repo_list.append(df[df['id'] == element[0]].values[0])
      i=i+1
      if i>15:
        break

  return repo_list"""
