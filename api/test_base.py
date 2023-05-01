from api.base import Base
from api.logger import get_script_logger
from tests.physical_test_view import PhysicalTestView
logger = get_script_logger()


class TestView(PhysicalTestView):
  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.base = Base()

  # pytest -v -s tests/searcher/helpers/test_sn.py -k test_sn
  def test_sn(self) -> None:
    logger.debug(self.base.drive_letter)
