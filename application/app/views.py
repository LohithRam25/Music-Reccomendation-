from django.shortcuts import render
import pickle
from fuzzywuzzy import fuzz,process
# Create your views here.
from django.http import HttpResponse
def home(request):
    if request.method=="POST":
        music_input=request.POST["song_name"]
        print(music_input)
        with open("D:\\MACHINE LEARNING\\PROJECTS\\Music Reccomendation\\model.pkl", "rb") as model1:
            model = pickle.load(model1)
        with open("D:\\MACHINE LEARNING\\PROJECTS\\Music Reccomendation\\vectors.pkl", "rb") as vector1:
            vectors = pickle.load(vector1)
        with open("D:\\MACHINE LEARNING\\PROJECTS\\Music Reccomendation\\data.pkl", "rb") as data1:
            data = pickle.load(data1)

        #hai = data.index[data["track_name"].str.lower() == music_input.lower()].tolist()
        track_names=data["track_name"].tolist()
        best_match = process.extractOne(music_input, track_names, scorer=fuzz.partial_ratio)
        if best_match:
            if fuzz.ratio(best_match[0],music_input) > 30: # If similarity score is above 80
                hai=best_match[0]
                index_of=track_names.index(hai)
                distances, indices = model.kneighbors(vectors[index_of].reshape(1, -1))
                reccomendations=[]
                for i in indices.flatten():
                    reccomendations.append([data["track_name"].iloc[i],data["track_artist"].iloc[i]])
                return render(request,"home.html",{"reccomendations":reccomendations})
            else:
                msg="Sorry!!! We Cannot Find the songs That are similar to the song.. Kindly check the spelling of the song You have entered or try another song"
                return render(request, "home.html", {"msg": msg})




        #for i in indices.flatten():
          #  print(data["track_name"].iloc[i] + " " + data["track_artist"].iloc[i])
        #return render(request,"home.html")
    else:
        return render(request, "home.html")