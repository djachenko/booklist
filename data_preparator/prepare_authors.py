import csv


def read_authors(filename):
    with open(filename) as authors_csv:
        reader = csv.DictReader(authors_csv, delimiter=";")

        authors = [row for row in reader]

        return authors


def handle_subauthor(subauthor):
    names = subauthor.rsplit(maxsplit=1)

    first = None
    middle = None

    if len(names) > 1 and names[1].endswith("."):
        last = names[0]

        other = [s for s in names[1].split(".") if s.strip()]

        first = other[0]

        if len(other) > 1:
            middle = other[1]
    elif len(subauthor.split()) == 2 and all(("." not in name for name in names)):
        first = names[0]
        last = names[1]
    elif len(subauthor.split()) == 3:
        names = subauthor.split()

        first = names[0]
        middle = names[1].strip(".")
        last = names[2]
    else:
        last = subauthor

    if first and len(first) <= 2:
        first += "."

    if middle and len(middle) <= 2:
        middle += "."

    return last, first, middle


def prepare_authors(authors):
    register = {}

    for author in authors:
        sub_authors = [sub_author.strip() for sub_author in author["Name"].split(", ")]
        handled_sub_authors = [handle_subauthor(sub_author) for sub_author in sub_authors]

        for handled_sub_author in handled_sub_authors:
            if handled_sub_author not in register:
                register[handled_sub_author] = len(register)

        handled_sub_authors_ids = [register[handled_sub_author] for handled_sub_author in handled_sub_authors]

        author["Name"] = handled_sub_authors_ids

    return register


def build_name(author):
    name = author[0]

    if author[1]:
        name += " " + author[1]

        if len(author[1]) <= 2:
            name += "."

    if author[2]:
        if not len(author[1]) <= 2:
            name += " "

        name += author[2]

        if len(author[2]) <= 2:
            name += "."

    name += "\n"

    return name


def write_authors(filename, authors):
    with open(filename, "w") as result:
        writer = csv.DictWriter(result, authors[0].keys())
        writer.writeheader()
        writer.writerows(authors)


def main():
    raw_authors = read_authors("authors_manual.csv")

    raw_authors = sorted(raw_authors, key=lambda x: int(x["Id"]))

    prepared_authors = prepare_authors(raw_authors)

    # write_authors("handled_authors.csv", prepared_authors)

    with open("register.csv", "w") as result:
        for name in sorted([build_name(prepared_author) for prepared_author in prepared_authors]):
            result.write(name)


if __name__ == '__main__':
    main()
