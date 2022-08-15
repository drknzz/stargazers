from typing import List, Optional
from pathlib import Path
import sys
import re

from bs4 import BeautifulSoup
import requests


class Stargazer:
    """ Stargazer representation """

    def __init__(self, name: str, avatar: str) -> None:
        self.name = name
        self.avatar = avatar


    def url(self):
        return "https://github.com/" + self.name


    def __str__(self):
        return f"Stargazer {self.name}"


class ReadMe:
    """ ReadMe file """

    COMMENT_TAG = "<!-- latest_stargazers -->"

    def __init__(self, path: Path) -> None:
        self.path = path
        self.content = self.read()


    def make_a_tag(self, src: str, content: str) -> str:
        return f'<a href="{src}">{content}</a>'


    def make_img_tag(self, src: str, width: Optional[int] = 60) -> str:
        return f'<img src="{src}" width="{width}px">'


    def make_table(self, stargazers: List[Stargazer], size: Optional[int] = 8) -> str:
        size = min(size, len(stargazers))
        table = "| "

        for stargazer in stargazers[:size]:
            table += f" {stargazer.name} |"
        
        table += "\n"
        table += "| " + " :-: |" * size
        table += "\n"
        table += "| "

        for stargazer in stargazers[:size]:
            table += f" {self.make_img_tag(stargazer.avatar)} |"

        table += "\n"

        return table


    def update(self, stargazers: List[Stargazer]):
        matches = re.finditer(self.COMMENT_TAG, str(self.content))
        positions = [m.span() for m in matches]

        starts, ends = positions[::2], positions[1::2]
        
        table = self.make_table(stargazers)

        for start, end in zip(starts, ends):
            self.replace(start[0], end[1], self.wrap_in_comment_tag(table))

        self.write()


    def wrap_in_comment_tag(self, content):
        return f"{self.COMMENT_TAG}\n{content}{self.COMMENT_TAG}\n"


    def read(self) -> str:
        with open(self.path, "r") as f:
            return f.read()


    def write(self, content: Optional[bytes] = None) -> None:
        with open(self.path, "w") as f:
            f.write(content or self.content)


    def replace(self, start, end, content) -> None:
        self.content = self.content[:start] + content + self.content[end:]


def fetch_stargazers(url: str) -> List[Stargazer]:
    """ Fetches a list of Stargazer objects """

    page_content = requests.get(url)
    soup = BeautifulSoup(page_content.content, "html.parser")

    stargazers_li = soup.find("ol").find_all("li")
    stargazers = []

    for li in stargazers_li:
        stargazer = Stargazer(
            name=li.find("h3").find("a").text,
            avatar=li.find("img")["src"],
        )
        stargazers.append(stargazer)
    
    return stargazers


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(f"Usage: python stargazers.py <URL_TO_REPOSITORY> <PATH_TO_README>")

    REPO_URL = sys.argv[1]
    URL = REPO_URL + '/stargazers'

    stargazers = fetch_stargazers(URL)

    root_path = Path(sys.argv[2]).parent.resolve()
    readme_path = root_path / "README.md"

    readme = ReadMe(readme_path)
    readme.update(stargazers)
    

if __name__ == "__main__":
    main()
