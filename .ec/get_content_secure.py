import sys, os, sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from hashlib import sha1

connect = sqlite3.connect("acmipc.db")
cursor = connect.cursor()
h = sha1()

# def main(args="https://www.acmicpc.net/problem/1463"):
def main(args):
    link = f"https://www.acmicpc.net/problem/{args}" if args.isnumeric() else args
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
    h.update(title.encode('utf-8'))
    title_hexed = h.hexdigest()
    description = content.find('div', { "id" : "problem_description" }).getText().strip()
    in_cond = content.find('section', { "id" : "input" }).getText().strip()
    out_cond = content.find('section', { "id" : "output" }).getText().strip()
    limits = content.find('div', { "id" : "problem_limit" }).getText().strip()
    samples = content.find_all(class_ = "sampledata")
    examples = ""
    file = None
    for i, sample in enumerate(samples):
        example_txt = sample.getText().strip()
        idx = int(i/2) + 1
        examples += """## 예제 {iotext} {idx}\n\n```\n{data}\n```\n\n""".format(iotext="입력" if i%2 == 0 else "출력", idx=idx, data=example_txt)
        if i%2 == 0:
            file = open(f"{title_hexed}/input{idx}.txt", "w")
        else:
            file = open(f"{title_hexed}/output{idx}.txt", "w")
        file.write(example_txt)
        file.close()

    readme_content = """# [{title}]({link})\n\n{description}\n\n# {in_cond}\n\n# {out_cond}\n\n# 제한조건\n\n{limits}\n\n{examples}""".format(
        title=title, description=description, link=link, in_cond=in_cond, out_cond=out_cond, limits=limits, examples=examples
    )

    file = open(f"{title_hexed}/README.md", "a")
    file.write(readme_content)
    file.close()
    print(title)
    print(len(samples) // 2)
if __name__ == '__main__':
    # main()
    main(sys.argv[1])