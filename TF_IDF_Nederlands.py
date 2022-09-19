from sklearn.feature_extraction import TfidfVectorizer
import sys


#input
# TODO replace with sys.argv, where argv is the list of locations of the cleaned documents
corpus = sys.argv

#functions
# TODO replace "corpus" with "filename=corpus", "het_features_names_out()" is unnecessary
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(filename=corpus)
vectorizer.get_feature_names_out()

#output
# TODO return "X" to UiPath

print(X.shape)
(4, 9)



