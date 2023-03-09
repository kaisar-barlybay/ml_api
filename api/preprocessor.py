from api.base import Base
from api.normalizer import Normalizer
import re
import string
import spacy
from nltk.corpus import stopwords
stop = set(stopwords.words('russian'))


class Preprocessor(Base):
  def __init__(self) -> None:
    super().__init__()
    self.normalizer = Normalizer()
    self.nlp = spacy.load("ru_core_news_sm")

  def tokenize(self, text: str):
    try:
      regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
      text = regex.sub(" ", text)  # remove punctuation
      doc = self.nlp(text)
      tokens = [token.lemma_ for token in doc]
      tokens = list(filter(lambda t: t.lower() not in stop, tokens))
      filtered_tokens = [w for w in tokens if re.search('[а-яА-Я]', w)]
      filtered_tokens = [w.lower() for w in filtered_tokens if len(w) >= 3]

      return filtered_tokens

    except TypeError as e:
      print(text, e)
      return None
