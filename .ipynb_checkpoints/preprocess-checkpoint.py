import nltk

nltk.download('stopwords') # stop  word in english
nltk.download('wordnet') # vocabulary for lemmatization
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re


def process_review(review):
    # convert review into lowercases
    review_lower=review.lower()

    # Remove punctuations, numbers
    review_puncs_nums_removed=re.sub(r"[^a-z\s]","",review_lower)

    # Tokenize the review: Convert sentence into words
    review_tokens=word_tokenize(review_puncs_nums_removed)

    # REmove stopword
    stop_words=stopwords.words('english')
    review_tokens_stopwords_removed=[token for token in review_tokens if token not in stop_words]

    # Lemmatization
    lemmatizer=WordNetLemmatizer()
    lemmatized_tokens=[lemmatizer.lemmatize(token, pos='n') for token in review_tokens_stopwords_removed]

    # Put together all the tokens as a single string object
    return " ".join(lemmatized_tokens)





if __name__=="__main__":
    review="The product was really nice!!!!"
    print (process_review(review))