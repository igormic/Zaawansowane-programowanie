import csv
from fastapi import FastAPI
from models import Link, Movie, Rating, Tag

app = FastAPI(title="Movies REST API")


def load_csv_as_objects(filepath: str, model_cls, column_keys: list[str]) -> list[dict]:
    serialized_items = []
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            args = [row[col] for col in column_keys]
            obj = model_cls(*args)
            serialized_items.append(obj.__dict__)
    return serialized_items


@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/movies")
def get_movies():
    return load_csv_as_objects(
        "data/movies.csv",
        Movie,
        ["movieId", "title", "genres"]
    )


@app.get("/links")
def get_links():
    return load_csv_as_objects(
        "data/links.csv",
        Link,
        ["movieId", "imdbId", "tmdbId"]
    )


@app.get("/ratings")
def get_ratings():
    return load_csv_as_objects(
        "data/ratings.csv",
        Rating,
        ["userId", "movieId", "rating", "timestamp"]
    )


@app.get("/tags")
def get_tags():
    return load_csv_as_objects(
        "data/tags.csv",
        Tag,
        ["userId", "movieId", "tag", "timestamp"]
    )