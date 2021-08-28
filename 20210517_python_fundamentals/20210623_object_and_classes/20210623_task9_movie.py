# Task 9 - Movie

class Movie:
    __watched_movies = []

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.__watched_movies.append(1)
        self.watched = True

    def __repr__(self):
        watched_movies_total = sum(self.__watched_movies)
        return f"Movie name: {self.name}; Movie director: {self.director}. " \
               f"Total watched movies: {watched_movies_total}"
