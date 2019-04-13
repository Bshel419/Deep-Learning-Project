import csv
import numpy as np

NUM_USERS = 610
learning_rate = 0.3
SIGMA = 0.5
LOOP = 100

genreKey = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', 'IMAX', '(no genres listed)']

mFile = open('ml-latest-small/movies.csv', encoding = 'utf-8')
movieFile = list(csv.reader(mFile, delimiter = ','))
movieFile.pop(0)

rFile = open('ml-latest-small/ratings.csv')
ratingsFile = list(csv.reader(rFile, delimiter = ','))
ratingsFile.pop(0)

#movies[movie#] = name
movies = {}
#genres[movie#] = [nGenres]
genres = {}
#ratings[user#] = (movie#, rating)
ratings = {}
#genreX[movie#] = [genre%]
genreX = {}
#theta[user#] = [genrePreferences]
theta = {}

for line in movieFile:
    movies[line[0]] = line[1]
    genres[line[0]] = line[2].split('|')

for x in range(NUM_USERS):
    ratings[str(x+1)] = []
    theta[str(x+1)] = np.random.uniform(size=len(genreKey))

for line in ratingsFile:
    ratings[line[0]].append((line[1], line[2]))

for k in movies:
    genreX[k] = np.zeros(len(genreKey))

counter = 0


for k in genres:
    for genre in genres[k]:
        counter += 1
    for genre in genres[k]:
        genreX[k][genreKey.index(genre)] = 1 / counter
    counter = 0

for n in range(NUM_USERS):
    for k in ratings:
        m = len(ratings[k]) - 1
        movieSum = 0

        for x in range(1, (m-1)):
            y = ratings[k][x][1]
            movieSum += ((theta[k].T * genreX[ratings[k][x][0]]) - float(y)) * genreX[ratings[k][x][0]]

        theta[k] = theta[k] - learning_rate * movieSum
    print(theta['2'])
        
        


