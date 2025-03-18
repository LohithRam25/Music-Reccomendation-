import pickle
with open("knn_model.pkl","rb") as model1:
  model=pickle.load(model1)
with open("vectors.pkl","rb") as vector1:
  vectors=pickle.load(vector1)
with open("data.pkl","rb") as data1:
  data=pickle.load(data1)
song_index = 33
distances, indices = model.kneighbors(vectors[song_index].reshape(1, -1))
print("Indices of similar songs:", indices.flatten())

for i in indices.flatten():
  print(data["track_name"].iloc[i])