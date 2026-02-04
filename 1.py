import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('stopwords')

text = "The quick BROWN foxes... they are JUMPING 10 lazy dogs!"

text = text.lower()

text = re.sub(r"[^a-z\s]", "", text)

stemmer = PorterStemmer()

stop_words = set(stopwords.words('english'))

res = [stemmer.stem(word) for word in text.split() if word not in stop_words]

print(res)