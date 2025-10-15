import dataclasses
from enums import OutputType


@dataclasses.dataclass
class ReportData:
    file: str
    line: int
    url: str
    result: str
    code: int
    reason: str


def generate(data: ReportData, type: OutputType):
    pass


def console(data: ReportData):
    line = ""
