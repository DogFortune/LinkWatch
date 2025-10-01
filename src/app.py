import argparse
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def check_link(url: str):
    try:
        res = urlopen(url, timeout=5)
        return {"result": True, "code": res.code, "url": res.url}
    except HTTPError as e:
        return {"result": False, "code": e.code, "url": e.url}
    except URLError as e:
        return {"result": False, "code": e.code, "url": e.url}


def extract_link(files: list):
    links = []
    # 欲しいのはファイル名と行数とリンク
    for file_path in files:
        with open(file_path, "r") as f:
            lines = f.readlines()
            item = {"filePath": file_path, "data": []}
            for i, line in enumerate(lines):
                if "http" in line:
                    item["data"].append({"line": i + 1, "link": line})
        links.append(item)
    return links


def lookup_file(path: str, filter="*.md"):
    # 指定したディレクトリから検査対象のファイルを抽出します。デフォルトはmdです。
    p = Path(path)
    files = [str(item) for item in p.rglob(filter)]
    return files


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", action="store_true", help="Increase verbosity")
    group.add_argument("--quiet", action="store_true", help="Decrease verbosity")
    return parser


def main(args=None):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    files = lookup_file(parsed_args.src)
    return files


if __name__ == "__main__":
    main()
