from tensorflow.keras.preprocessing.text import text_to_word_sequence
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import pickle



def stop_Words():
    with open("stopwords.txt", 'r') as f:
        stop_words = f.read().splitlines()
    return stop_words


stop_words = set(stop_Words())


def create_L():
    L = []
    f = open('reviews.txt', 'r')
    for review in f.readlines():
        words = text_to_word_sequence(review)
        L += list(words)
    W =[]
    for word in L:
        if word not in stop_words and word.isalpha() and len(word)>2:
            W.append(word)

    word_counts = Counter(W)

    return L,W,word_counts

print("Creating L , W and word counts...")

L, W, word_counts = create_L()

common_words_with_count = word_counts.most_common(500).copy()

print("Top 500 common words with their count:")
print(common_words_with_count)

common_words =[]
for words in common_words_with_count:
     common_words.append(words[0])


# vector = []
# vector.append(common_words)
# temp_vector = [0]*len(common_words)

print("Vectorizing...")

vectorizer = CountVectorizer(decode_error='ignore',strip_accents='unicode', vocabulary= common_words)
reviews = open('reviews.txt')
vector = vectorizer.fit_transform(reviews).toarray()

print("Done Vectorizing")


# print(vector)
# print(vectorizer.vocabulary_)
# print(vector)

# f = open("file.csv", 'w')
#
# for v in vectorizer.vocabulary_:
#     f.write("%s,"%v)
#
# f.write("\n")
#
# for v in vector:
#     for i in range(len(v)):
#         f.write("%s,"%v[i])
#     f.write('\n')

# print("Saving file to words.pickle ..")
#
# pickle_out = open("words.pickle","wb")
# # pickle.dump(common_words, pickle_out)
# pickle.dump(vector, pickle_out)
# pickle_out.close()
#
# print("Done Saving.")