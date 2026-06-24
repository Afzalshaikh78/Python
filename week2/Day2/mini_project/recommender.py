import ast
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge and select relevant columns
movies = movies.merge(credits, on="title")
movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
movies.dropna(inplace=True)

# Helper functions
def convert(text):
    return [item["name"] for item in ast.literal_eval(text)]

def convert_cast(text):
    return [item["name"] for item in ast.literal_eval(text)[:3]]

def fetch_director(text):
    for item in ast.literal_eval(text):
        if item["job"] == "Director":
            return [item["name"]]
    return []

# Apply transformations
movies["genres"]   = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"]     = movies["cast"].apply(convert_cast)
movies["crew"]     = movies["crew"].apply(fetch_director)
movies["overview"] = movies["overview"].apply(lambda x: x.split())

# Remove spaces from multi-word names so vectorizer treats them as single tokens
for col in ["genres", "keywords", "cast", "crew"]:
    movies[col] = movies[col].apply(lambda x: [i.replace(" ", "") for i in x])

# Build tags column
movies["tags"] = movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"]

# Create final dataframe
new_df = movies[["movie_id", "title", "tags"]].copy()
new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x).lower())

# Vectorize
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(new_df["tags"]).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Recommend function
def recommend(movie):
    movie = movie.strip()
    matches = new_df[new_df["title"].str.lower() == movie.lower()]

    if matches.empty:
        print(f"Movie '{movie}' not found!")
         return

    actual_title = matches.iloc[0]["title"]
    movie_index = matches.index[0]

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print(f"\nMovies similar to '{actual_title}':\n")
    for item in movies_list:
        print(new_df.iloc[item[0]].title)

# Save to pickle
pickle.dump(new_df, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

# Test
# recommend("Avengers: Age of Ultron")


recommend("Iron Man")