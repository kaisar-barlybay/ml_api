from pandas import DataFrame
from api.base import Base
import re
from nltk.corpus import stopwords
import string
from tqdm import tqdm
import pandas as pd
import spacy
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;+-]')
BAD_SYMBOLS_RE = re.compile('[^0-9а-я #+_]')
PUNCTUATION = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')


class Normalizer(Base):
  def __init__(self) -> None:
    super().__init__()
    self.stops_ru = set(stopwords.words('russian'))
    self.stops_en = set(stopwords.words('english'))

  def clean_text(self, text: str, lang_code: str = 'en', stops: list[str] = []) -> str:
    try:
      match lang_code:
        case 'en':
          stops += self.stops_en
        case 'ru':
          stops += self.stops_ru
        case _:
          stops += self.stops_en
      stops = set(stops)

      text = text.lower()
      # text = REPLACE_BY_SPACE_RE.sub(' ', text)
      # text = BAD_SYMBOLS_RE.sub(' ', text)
      text = PUNCTUATION.sub(' ', text)  # remove punctuation
      doc = self.nlp(text)
      tokens = [token.lemma_ for token in doc]
      # ? mb implement that
      # from nltk.tokenize import WhitespaceTokenizer
      # wt = WhitespaceTokenizer()
      # words = wt.tokenize(text)

      def filter_f(w):
        return w.lower() not in stops and len(w) >= 3 and re.search('[а-яА-Я]', w)

      filtered_tokens = [w.lower() for w in tokens if filter_f(w)]
      text = ' '.join(filtered_tokens)
      return text
    except Exception as e:
      print(text, e)
      return text

  def norma_pipeline(self, df: DataFrame):
    tosk = {
        # 'kstru_parent_name': ('kstru_group_name_normalized', {}),
        # 'CATEGORY2': ('kstru_name_normalized', {}),
        # 'ENSTRU_NAMERU': ('enstru_name_normalized', {}),
        # 'ENSTRU_DESCRIPTIONRU': ('enstru_description_normalized', {}),
        'NAME': ('name_normalized', {}),
    }
    for col_name, (_, d) in tosk.items():
      for cat_name in tqdm(df[col_name].unique()):
        if not pd.isnull(cat_name):
          d[cat_name] = self.clean_text(cat_name, 'ru')
    for col_name, (target_col_name, d) in tosk.items():
      df[target_col_name] = df[col_name].apply(lambda x: None if pd.isnull(x) else d[x])
    return df
