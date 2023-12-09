import pandas as pd
import requests
import numpy as np

# Define the URL for movie data
myurl = "https://liangfgithub.github.io/MovieData/movies.dat?raw=true"

# Fetch the data from the URL
response = requests.get(myurl)

# Split the data into lines and then split each line using "::"
movie_lines = response.text.split('\n')
movie_data = [line.split("::") for line in movie_lines if line]

# Create a DataFrame from the movie data
movies = pd.DataFrame(movie_data, columns=['movie_id', 'title', 'genres'])
movies['movie_id'] = movies['movie_id'].astype(int)

genres = list(
    sorted(set([genre for genres in movies.genres.unique() for genre in genres.split("|")]))
)

top_movies_per_genre_df = pd.read_csv('https://raw.githubusercontent.com/yiboli1990/proj4_1/main/top_movies_per_genre.csv')

def get_highly_rated_movies(genre: str):
    if genre in top_movies_per_genre_df.columns:
        # Get the movie IDs for the specified genre
        movie_ids = top_movies_per_genre_df[genre].dropna().astype(int).tolist()

        # Ensure the movies DataFrame has 'movie_id' as int for proper merging
        movies['movie_id'] = movies['movie_id'].astype(int)

        # Filter movies DataFrame for those IDs
        popular_movies = movies[movies['movie_id'].isin(movie_ids)]

        # Ensure the order is the same as in the CSV by setting a categorical
        # with the order defined by the CSV list
        movies_order = pd.Categorical(
            popular_movies['movie_id'],
            categories=movie_ids,
            ordered=True
        )
        popular_movies = popular_movies.assign(order=movies_order)
        popular_movies = popular_movies.sort_values('order').drop('order', axis=1).head(10)

        return popular_movies
    else:
        return pd.DataFrame()


def myIBCF(new_user, sim_matrix_url):
    # Load the similarity matrix
    sim_matrix = pd.read_csv(sim_matrix_url, index_col=0)

    # Initialize a dictionary to hold predicted ratings
    predictions = {}

    # Loop through each movie
    for movie in sim_matrix.columns:
        if pd.isna(new_user[movie]):  # Check if the movie is unrated by the new user
            # Select the top 30 similar movies
            top_movies = sim_matrix.loc[movie].dropna()
            top_movies = top_movies[top_movies.index.isin(new_user.index)]
            
            # Check for overlapping ratings
            overlapping_movies = top_movies.index[top_movies.index.isin(new_user.dropna().index)]
            if overlapping_movies.empty:
                continue  # Skip if no overlapping ratings

            # Compute prediction
            numer = sum(top_movies[overlapping_movies] * new_user[overlapping_movies])
            denom = sum(top_movies[overlapping_movies])
            if denom != 0:
                prediction = numer / denom
                predictions[movie] = prediction
            else:
                predictions[movie] = np.nan

    top_recommendations = sorted(predictions.items(), key=lambda x: x[1], reverse=True)[:10]

    # Check if we have fewer than 10 recommendations
    if len([rec for rec in top_recommendations if not pd.isna(rec[1])]) < 10:
        # Number of additional recommendations needed
        additional_needed = 10 - len([rec for rec in top_recommendations if not pd.isna(rec[1])])

        # Get movies not rated by the user
        unrated_movies = ratings_matrix.columns[ratings_matrix.loc[new_user.name].isna()]
        
        # For simplicity, pick the most-rated movies as additional recommendations
        most_rated_movies = ratings_matrix.count().sort_values(ascending=False)
        additional_recommendations = [(movie, np.nan) for movie in most_rated_movies.index if movie not in [rec[0] for rec in top_recommendations] and movie in unrated_movies]

        # Append these additional recommendations to the list
        top_recommendations.extend(additional_recommendations[:additional_needed])

    # Extract only the movie IDs from the top recommendations and convert them to integers
    top_movie_ids = [int(movie_id[1:]) for movie_id, _ in top_recommendations]  # Remove 'm' prefix and convert to integer

    return top_movie_ids

    # Check if we have fewer than 10 recommendations
    if len([rec for rec in top_recommendations if not pd.isna(rec[1])]) < 10:
        # Number of additional recommendations needed
        additional_needed = 10 - len([rec for rec in top_recommendations if not pd.isna(rec[1])])

        # Get movies not rated by the user
        unrated_movies = ratings_matrix.columns[ratings_matrix.loc[new_user.name].isna()]
        
        # For simplicity, pick the most-rated movies as additional recommendations
        most_rated_movies = ratings_matrix.count().sort_values(ascending=False)
        additional_recommendations = [(movie, np.nan) for movie in most_rated_movies.index if movie not in [rec[0] for rec in top_recommendations] and movie in unrated_movies]

        # Append these additional recommendations to the list
        top_recommendations.extend(additional_recommendations[:additional_needed])

def get_displayed_movies():
    return movies.head(100)

def get_recommended_movies(new_user_ratings):
    # Load the similarity matrix
    sim_matrix = pd.read_csv('https://raw.githubusercontent.com/yiboli1990/proj4_1/main/processed_similarity_matrix.csv', index_col=0)

    # Initialize a new Series with NaN values and an index that matches the similarity matrix
    new_user_ratings_series = pd.Series([np.nan] * len(sim_matrix.columns), index=sim_matrix.columns)

    # Update the series with the new user ratings
    # Prefix the movie IDs with 'm'
    for movie_id, rating in new_user_ratings.items():
        movie_key = 'm' + str(movie_id)
        if movie_key in new_user_ratings_series.index:
            new_user_ratings_series[movie_key] = rating
    
    top_movie_ids = myIBCF(new_user_ratings_series, 'https://raw.githubusercontent.com/yiboli1990/proj4_1/main/processed_similarity_matrix.csv')
    # Return the top recommendations
    # Create a DataFrame from the list of recommended movie IDs
    recommended_movies_df = pd.DataFrame(top_movie_ids, columns=['movie_id'])

    # Merge with the movies DataFrame to get full movie details
    recommended_movies_df = recommended_movies_df.merge(movies, on='movie_id')

    return recommended_movies_df

