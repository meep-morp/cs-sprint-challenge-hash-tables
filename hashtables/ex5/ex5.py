# Your code here


def finder(files, queries):
    result = []
    file_d = {}

    # Store queries in a dictionary
    for x in queries:
        file_d[x] = x

    for i in files:
        # Split at the '/'
        words = i.split("/")
        # If the last string in the path matches a query, return it
        if words[-1] in file_d:
            result.append(i)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
