import os
from pathlib import Path
from pandas import DataFrame, ExcelWriter


class Base:
  def __init__(self) -> None:
    self.drive_letter = os.getcwd()[:3]

  def check_create_dir(self, path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

  def file_or_dir_exists(self, path: str) -> bool:
    return os.path.exists(path)

  def to_csv(self, df: DataFrame, path: str, sort_values: list[str] = []):
    df.sort_values(by=sort_values).to_csv(path, encoding='utf-8-sig', index=False)

  def to_excel(self, df: DataFrame, path_or_sheetname: str, sort_values: list[str] = [], writer: ExcelWriter | None = None, index: bool = False):
    if writer is None:
      df.sort_values(by=sort_values).to_excel(path_or_sheetname, encoding='utf-8-sig', index=index)
    else:
      df.sort_values(by=sort_values).to_excel(writer, sheet_name=path_or_sheetname, encoding='utf-8-sig', index=index)

  def to_excel_book(self, path: str, df_sheet_names: list[tuple[DataFrame, str, list[str]]]):
    with ExcelWriter(path) as writer:
      for df, sheet_name, sort_values in df_sheet_names:
        self.to_excel(df, path_or_sheetname=sheet_name, sort_values=sort_values, writer=writer)

