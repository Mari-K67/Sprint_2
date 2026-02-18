class Movies:
    def __init__(self, movies=None):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies
        
class Comedy(Movies):
    def __init__(self, movies=None):
        super().__init__(movies)
        
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f'Комедии: {self.movies}')

class Drama(Movies):
    def __init__(self, movies=None):
        super().__init__(movies)
        
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f'Драмы: {self.movies}')
        
comedy_1 = Comedy()
comedy_1.add_movie('Большой куш')

drama_1 = Drama()
drama_1.add_movie('Оружейный барон')