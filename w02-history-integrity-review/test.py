import csv
from itertools import islice
f = open('imdb.csv', 'r')
f.readline()
reader = csv.reader(f, delimiter='\t')
title = []
year = []
rating = []
vote = []
for row in islice(reader, 0, None):
    title.append(row[0])
    year.append(int(row[1]))
    rating.append(float(row[2]))
    vote.append(int(row[3]))
print (title[:10])
print (title[-1])
print (len(vote))


for t in title[-20:]:
    print (t)