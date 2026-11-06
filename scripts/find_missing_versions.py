#!/usr/bin/env python

import json
import re
import subprocess
from html.parser import HTMLParser
from urllib.request import urlopen


class SparkVersions(HTMLParser):
    def __init__(self):
        super().__init__()
        self.versions = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            match = re.fullmatch(r"spark-(\d+\.\d+\.\d+)/", href)
            if match:
                self.versions.add(match.group(1))


def missing_versions(listing, tags):
    parser = SparkVersions()
    parser.feed(listing)
    return sorted(version for version in parser.versions if f"v{version}" not in tags)


if __name__ == "__main__":
    with urlopen("https://dlcdn.apache.org/spark/", timeout=30) as response:
        listing = response.read().decode("utf-8")
    tags = subprocess.check_output(["git", "tag", "--list"], text=True).splitlines()
    print(json.dumps(missing_versions(listing, set(tags)), separators=(",", ":")))
