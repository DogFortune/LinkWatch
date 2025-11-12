import dataclasses
from pprint import pformat
import json


@dataclasses.dataclass
class ReportData:
    file: str
    line: int
    url: str
    result: str
    code: int
    reason: str


def console(data: list[ReportData]):
    # TODO: 出力形式は仮でpformatを設定中。
    line = pformat(data)
    return line


def json_dump(data: list[ReportData], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
