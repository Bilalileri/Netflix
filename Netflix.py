import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("C:/Users/Bilal İLERİ/Desktop/Data Science/Introduction to Data Science/netflix_data.csv") #Load and inspect the Netflix data

netflix_subset = netflix_df.loc[netflix_df["type"] == "Movie"] #Subset the DataFrame for "Movies" (first true or false identification and then creating dataframe)
netflix_movies = netflix_subset[["title","country","genre","release_year","duration"]] #Subset the columns of the new DataFrame(if there is more than one column then double bracet)
short_movies = netflix_movies[netflix_movies["duration"] < 60] #Filter the DataFrame by Movie duration
colors= [];
for i,j in netflix_movies.iterrows():
    if j["genre"] == "Children":
        colors.append("red")
    elif j["genre"] == "Documentaries":
        colors.append("green")
    elif j["genre"] == "Stand-Up":
        colors.append("blue")
    else :
        colors.append("black")    
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()
answer = "no , scatter plot doesn't say so :)"
print("Are we certain that movies are getting shorter? : " + answer)