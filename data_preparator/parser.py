import csv
import json

from data_preparator.prepare_authors import prepare_authors


def read(filename):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")

        objects = [row for row in reader]

        return objects


def project(source, names):
    result = [{name: element[name] for name in names} for element in source]

    return result


def cast_field_to_int(elements, key="Id", default=0):
    for element in elements:
        if element[key]:
            element[key] = int(element[key])
        else:
            element[key] = default


def shift_int_field(elements, key="Id", step=-1):
    for element in elements:
        element[key] += step


def extract_from_column(table, column_name):
    extracted_data = {}

    for row in table:
        extracted = row[column_name]

        if extracted not in extracted_data:
            extracted_data[extracted] = len(extracted_data)

        row[column_name] = [extracted_data[extracted]]

    return extracted_data


def dict_to_list(data):
    return [{"Id": v, "Name": k} for k, v in data.items()]


def extract(books, column):
    authors = extract_from_column(books, column)
    authors_list = dict_to_list(authors)

    return authors_list


def to_book(obj):
    res = {
        "model": "list.book",
        # "pk": obj["Id"],
        "fields": {
            "author": obj["Author"],
            "name": obj["Title"].strip("."),
            "publisher": obj["Publisher"][0],
            "pages_amount": obj["Pages"],
        }
    }

    if obj["Storage"] >= 0:
        res["fields"]["storage"] = obj["Storage"]

    return res


def to_author(obj):
    name = obj["Name"]

    res = {
        "model": "list.author",
        "pk": obj["Id"],
        "fields": {
            "last_name": name[0],
            "first_name": name[1],
            "middle_name": name[2]
        }
    }

    return res


def to_publisher(obj):
    return {
        "model": "list.publisher",
        "pk": obj["Id"],
        "fields": {
            "name": obj["Name"]
        }
    }


def to_storage(obj):
    return {
        "model": "list.storage",
        "pk": obj["Id"],
        "fields": {
            "name": obj["Place"]
        }
    }


def sort_by_id(collection):
    return sorted(collection, key=lambda x: x["Id"])


def sort_by_name(collection):
    return sorted(collection, key=lambda x: x["Id"])


def to_json(books, authors, publishers, storages):
    return [to_author(i) for i in sort_by_id(authors)] + \
           [to_publisher(i) for i in sort_by_id(publishers)] + \
           [to_storage(i) for i in sort_by_id(storages)] + \
           [to_book(i) for i in sort_by_id(books)]


def main():
    books = read("books_input.csv")
    storages = read("storages_input.csv")

    storages = project(storages, ["Id", "Place"])

    cast_field_to_int(books, key="Id")
    shift_int_field(books, key="Id", step=-1)

    cast_field_to_int(books, "Storage", -1)
    cast_field_to_int(books, "Pages", 0)
    cast_field_to_int(books, "Year", -1)

    cast_field_to_int(storages, "Id")

    shift_int_field(books, "Storage", -1)
    shift_int_field(storages, "Id", -1)

    authors = extract(books, "Author")
    publishers = extract(books, "Publisher")

    authors = sorted(authors, key=lambda x: x["Id"])
    authors = read("authors_manual.csv")

    cast_field_to_int(authors, "Id")

    authors = sorted(authors, key=lambda x: x["Id"])

    prepared_authors = prepare_authors(authors)
    prepared_authors = dict_to_list(prepared_authors)
    prepared_authors = sorted(prepared_authors, key=lambda x: x["Id"])

    authors_list = {author["Id"]: author["Name"] for author in authors}

    for book in books:
        old_author = book["Author"][0]
        new_author = authors_list[old_author]
        book["Author"] = new_author

    with open("books.csv", "w") as result:
        writer = csv.DictWriter(result, books[0].keys())
        writer.writeheader()
        writer.writerows(books)

    with open("authors.csv", "w") as result:
        writer = csv.DictWriter(result, ["Id", "Name"], delimiter=";")
        writer.writeheader()
        writer.writerows(sorted(authors, key=lambda x: int("," not in x["Name"])))

    with open("publishers.csv", "w") as result:
        writer = csv.DictWriter(result, publishers[0].keys())
        writer.writeheader()
        writer.writerows(publishers)

    with open("storages.csv", "w") as result:
        writer = csv.DictWriter(result, storages[0].keys())
        writer.writeheader()
        writer.writerows(storages)

    pre = to_json(books, prepared_authors, publishers, storages)

    j = json.dumps(pre, indent=4)

    with open("result.json", "w") as result:
        result.write(j)


if __name__ == '__main__':
    main()
