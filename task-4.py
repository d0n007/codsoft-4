# Sample movie data (Movie, Genre)
movies = [
    ("Movie A", ["Action", "Adventure"]),
    ("Movie B", ["Comedy", "Romance"]),
    ("Movie C", ["Action", "Comedy"]),
    ("Movie D", ["Drama"]),
    ("Movie E", ["Adventure", "Family"]),
]

# User preferences (Genre preferences)
user_preferences = ["Action", "Adventure"]

# Function to recommend movies based on user preferences
def recommend_movies(user_preferences, movies):
    recommended_movies = []
    for movie, genres in movies:
        # Calculate the Jaccard similarity between user preferences and movie genres
        intersection = set(user_preferences) & set(genres)
        union = set(user_preferences) | set(genres)
        similarity = len(intersection) / len(union)

        # Consider movies with a similarity score above a threshold (e.g., 0.5)
        if similarity > 0.5:
            recommended_movies.append(movie)
    
    return recommended_movies

# Get movie recommendations for the user
recommendations = recommend_movies(user_preferences, movies)

if recommendations:
    print("Recommended Movies:")
    for movie in recommendations:
        print(movie)
else:
    print("No recommendations found.")