class MovieCatalog:
    def __init__(self):
        '''
            Initializing of __init__. 
            Create a dictionary for saving directors (as key) and their movies.
        '''
        self.catalogo = {}

    def add_movie(self, director_name, movies):
        '''
            This function add movies of a director.
            input: director, movies
            return: None
        '''
        if director_name in self.catalogo:
            self.catalogo[director_name].update(movies)
        else:
            self.catalogo[director_name] = set(movies)

    def remove_movie(self, director_name, movie_name):
        '''
            This function remove movies of a director. 
            If some movies doesn't have a director, delete all the record.
            input: director, movies
            return: None
        '''
        if director_name in self.catalogo:
            if movie_name in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie_name)
                if not self.catalogo[director_name]:
                    del self.catalogo[director_name]

    def list_directors(self):
        '''
            This function return the list of each director
            input: None
            return: Directors
        '''
        return list(self.catalogo.keys())

    def get_movies_by_director(self, director_name):
        '''
            This function permit to find movies searching the director.
            input: director
            return: movies
        '''
        if director_name in self.catalogo:
            return list(self.catalogo[director_name])
        else:
            return []

    def get_movies_by_title(self, title):
        '''
            This function permit to find movies by their title.
            input: title of the movie
            return: movie            
        '''
        result = {}
        for director, movies in self.catalogo.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                result[director] = matching_movies
        if result:
            return result
        else:
            return "Nessun film trovato con il titolo cercato."