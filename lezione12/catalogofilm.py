class MovieCatalog():
    def __init__(self) -> None:
        self.catalogo : dict = {}

    def add_movie(self, director_name : str, movies:list):
        