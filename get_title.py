import sys, os, sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup

connect = sqlite3.connect("acmipc.db")
cursor = connect.cursor()

# def main(args="https://www.acmicpc.net/problem/1463"):
def main(args):
    link = args
    id = int(link.split("/")[-1])
    cursor.execute("CREATE TABLE IF NOT EXISTS RAW_TABLE (id integer PRIMARY_KEY, content blob)")
    cursor.execute("SELECT id, content FROM RAW_TABLE WHERE id = ?", (id,))
    found = cursor.fetchone()
    if not found:
        # if id do not exist, read from bs4
        content = BeautifulSoup(urlopen(link), 'html.parser')
        cursor.execute("INSERT INTO RAW_TABLE VALUES (?, ?)", (id, str(content)))
        connect.commit()
    else:
        (id_found, content_found) = found
        content = BeautifulSoup(content_found, 'html.parser')
    title = " ".join(content.title.getText().split(" ")[1:])
    print(title)
if __name__ == '__main__':
    # main()
    main(sys.argv[1])