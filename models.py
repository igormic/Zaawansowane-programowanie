class Movie:
    def __init__(self, movie_id: str, title: str, genres: str):
        self.movieId = int(movie_id)
        self.title = title
        self.genres = genres.split("|") if genres else []


class Link:
    def __init__(self, movie_id: str, imdb_id: str, tmdb_id: str):
        self.movieId = int(movie_id)
        self.imdbId = imdb_id
        self.tmdbId = int(tmdb_id) if tmdb_id else None


class Rating:
    def __init__(self, user_id: str, movie_id: str, rating: str, timestamp: str):
        self.userId = int(user_id)
        self.movieId = int(movie_id)
        self.rating = float(rating)
        self.timestamp = int(timestamp)


class Tag:
    def __init__(self, user_id: str, movie_id: str, tag: str, timestamp: str):
        self.userId = int(user_id)
        self.movieId = int(movie_id)
        self.tag = tag
        self.timestamp = int(timestamp)