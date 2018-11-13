# Part 1: imdb
# Part 2: Computing Summary Statistics

from imdbpie import Imdb
import string

imdb = Imdb()

mtr = {'Harry Potter and the Sorcerer\'s Stone':'tt0241527',
'Harry Potter and the Chamber of Secrets':'tt0295297', 'Harry Potter and the Prisoner of Azkaban':'tt0304141',
'Harry Potter and the Goblet of Fire':'tt0330373', 'Harry Potter and the Order of the Phoenix':'tt0373889',
'Harry Potter and the Half-Blood Prince':'tt0417741', 'Harry Potter and the Deathly Hallows: Part 1':'tt0926084',
'Harry Potter and the Deathly Hallows: Part 2':'tt1201607'}

# for key in mtr:
#     movietitle = key
#     movieid = mtr.get(movietitle)
#     print(imdb.search_for_title(movietitle)[0])
    
# movietitle = input('Write movie title: ')
# movieid = mtr.get(movietitle)
# print(imdb.search_for_title(movietitle)[0])

strippables = string.punctuation + string.whitespace

def process_file(filename):
    hist = {}
    fp = open(filename)
    for line in fp:
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1
    return hist


def process_review(movietitle, movieid):
    reviews = imdb.get_title_user_reviews(movieid)

    rv = reviews['reviews'][0]['reviewText']
    hist = {}

    strippables = string.punctuation + string.whitespace

    for word in rv.split():
        word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1
    
    return hist

# process_review(movietitle, movieid)

# hist = process_review(movietitle, movieid)

def most_common(hist, skip_stopwords=True):
# def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    """
    
    stopwords = process_file('Stopwords.txt')
    t = []
    
    for key, value in hist.items():
        if skip_stopwords:
            if key not in stopwords:
                t.append((value, key))
        else:
            t.append((value, key))

    t.sort()
    t.reverse()
    return t
# most_common(hist, skip_stopwords=True)
# print(most_common(hist))

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words and their frequencies in the review are:')
    for freq, word in t[:num]:
        print(word, '\t','\t','\t', freq)

# hist = process_review(movietitle, movieid)
# print_most_common(hist, num=10)

# import pprint
# pprint.pprint(reviews)

# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])

def main():
    for key in mtr:
        movietitle = key
        movieid = mtr.get(movietitle)
        print(imdb.search_for_title(movietitle)[0])
        hist = process_review(movietitle, movieid)

        print_most_common(hist, num=5)
    
        # t = most_common(hist)
        # print('The most common words are:')
        # for freq, word in t[0:5]:
        #     print(word, '\t', freq)

if __name__ == '__main__':
    main()