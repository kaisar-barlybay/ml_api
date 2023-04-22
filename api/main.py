from api.base import Base
from api.preprocessor import Preprocessor
from api.visualizer import Visualizer
from pandas import DataFrame
import os


class Main(Base):
  def __init__(self, **kwargs) -> None:
    super().__init__()
    self.visualizer = Visualizer()
    self.preprocessor = Preprocessor()
    self.src_path = os.path.join(self.drive_letter, 'src')

  def get_not_null_df(self, df: DataFrame, column_names: list[str]):
    for cn in column_names:
      df = df[~df[cn].isnull()]
    return df
