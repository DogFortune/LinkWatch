import argparse
from pathlib import Path


def lookup_file(path: str, filter="*.md"):
    p = Path(path)
    files = [str(item) for item in p.rglob(filter)]
    return files


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    return parser


def main(args=None):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    files = lookup_file(parsed_args.src)
    print(files)
    print(parsed_args.src)
    return files


if __name__ == "__main__":
    main()
