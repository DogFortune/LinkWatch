from dataclasses import dataclass
from dataclasses_json import dataclass_json
from linkstat.enums import Result
from typing import List
import json
import os
import shutil


@dataclass_json
@dataclass
class ReportData:
    file: str
    line: int
    url: str
    result: Result
    code: int
    reason: str


@dataclass_json
@dataclass
class ReportCollection:
    Reports: List[ReportData]


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # 例外オブジェクトを文字列に変換
        if isinstance(obj, Exception):
            return str(obj)
        return super().default(obj)


def summary(data: list[ReportData]):
    """サマリーを出力します。
    チェックしたURLの数、OK,NGの数、NGのものはURLを出す。

    :param data: _description_
    :type data: list[ReportData]
    :return: _description_
    :rtype: _type_
    """
    total_count = len(data)
    ok_count = sum(item.result == Result.OK for item in data)
    ng_items = [item for item in data if item.result == Result.NG]
    summary = f" {total_count} Total, {ok_count} OK, {len(ng_items)} NG "

    terminal_width = shutil.get_terminal_size().columns
    if terminal_width < 40:
        terminal_width = 80

    total_fill = terminal_width - len(summary)
    left_fill = total_fill // 2
    right_fill = total_fill - left_fill

    line = f"{"="*left_fill}{summary}{"="*right_fill}"
    return line


def dump_json(data: list[ReportData], output_path: str):
    if os.path.splitext(output_path)[-1].lower() != ".json":
        raise ValueError
    collection = ReportCollection(Reports=data)
    json_str = json.dumps(
        collection.to_dict(), indent=4, ensure_ascii=False, cls=CustomEncoder
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json_str)
