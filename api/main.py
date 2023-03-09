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
    self.__datasets_path = None
    self.__temp_path = None

  def get_not_null_df(self, df: DataFrame, column_names: list[str]):
    for cn in column_names:
      df = df[~df[cn].isnull()]
    return df

  @property
  def datasets_path(self):
    if self.__datasets_path is None:
      # self.__datasets_path = os.path.join(self.drive_letter, 'datasets')
      self.__datasets_path = 'my_datasets'
    return self.__datasets_path

  @property
  def temp_path(self):
    if self.__temp_path is None:
      # self.__datasets_path = os.path.join(self.drive_letter, 'temp')
      self.__temp_path = 'temp'
    return self.__temp_path
