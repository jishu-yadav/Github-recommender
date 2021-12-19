def fit(keywords):
  cv = CountVectorizer()

  count_matrix = cv.fit_transform(keywords)

  # print(count_matrix.toarray())

  cosine_sim = cosine_similarity(count_matrix) 
  return cosine_sim

def get_name_from_index(index):
		return df[df['index'] == index]["full_name"].values[0]

def get_index_from_owner(project_desc):
	return df[df.combined_features == project_desc]["index"].values[0]

def recommendations(cosine_sim,desc):
  contributor_index = get_index_from_owner(desc)

  similar_project =  list(enumerate(cosine_sim[contributor_index]))

  sorted_similar_project = sorted(similar_project, key=lambda x:x[1], reverse=True)

  # top 15

  #print("\nPROJECT DESCRIPTION:\n" , df[df['index'] == sorted_similar_project[0][0]]["combined_features"].values[0] , "\n")
  #print("RECOMMENDED REPOSITORIES:-\n")

  i=0
  repo_list=[]
  for element in sorted_similar_project:
      name = get_name_from_index(element[0])
      repo_list.append(df[df['index'] == element[0]].values[0])
      i=i+1
      if i>15:
        break

  return repo_list
