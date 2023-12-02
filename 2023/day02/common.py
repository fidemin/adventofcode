def preprocess(file):
    rows = []
    for line in file:
        rows.append(line.strip())

    return rows
