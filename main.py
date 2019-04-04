import csv
import numpy as np

genreKey = ['Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

mFile = open('ml-latest-small/movies.csv', encoding = 'utf-8')
movieFile = list(csv.reader(mFile, delimiter = ','))
movieFile.pop(0)

rFile = open('ml-latest-small/ratings.csv')
ratingsFile = list(csv.reader(rFile, delimiter = ','))

movies = {}
genreMovies = {}
genres = []

for line in movieFile:
    movies[line[0]] = line[1]
    genres.insert(int(line[0]), line[2].split('|'))

for genre in genreKey:
    genreMovies[genre] = []

for item in genres:
    print(genres.index(item))
    for genre in item:
        '''if genre in genreKey:
            genreMovies[genre].append(movies[str(genres.index(item))])
print(genreMovies)'''