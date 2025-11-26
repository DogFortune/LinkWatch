from dataclasses import dataclass
from dataclasses_json import dataclass_json
from linkstat.enums import Result
from pprint import pformat
from typing import List
import json
import os


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
    ok_count = len([item for item in data if item.result == Result.OK])
    ng_count = len([item for item in data if item.result == Result.NG])
    line = f"Total: {total_count} OK: {ok_count} NG: {ng_count}"
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
