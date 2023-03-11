file = open("refs.bib", "r")

entry = {}
entry_type = None
entry_key = None

def process(entry_key, entry_type, entry):
    entry_key = entry_key.lower()
    print(entry_key.lower(), entry_type)
    print(entry)
    abstract = None
    with open(f"_publications/{entry_key}.md", "w") as f:
        f.write("---\n")
        f.write("layout: publication\n")
        f.write(f"type: {entry_type}\n")
        f.write(f"key: {entry_key}\n")
        for k, v in sorted(list(entry.items())):
            if k == 'abstract':
                abstract = v
                continue
            f.write(f"{k}: \"{v}\"\n")
        f.write("---\n")
        if abstract:
            f.write(f"\n{abstract}\n")



for line in file.readlines():
    if not line.strip():
        if entry:
            process(entry_key, entry_type, entry)
        continue

    if line.startswith('@'):
        entry = {}
        entry_type = line[1:].split("{")[0]
        entry_key = line.strip()[len(entry_type)+2:-1]
        continue

    if line.strip() == "}":
        continue

    splits = line.split(None, 2)
    entry[splits[0].strip()] = splits[2].strip().strip(",")[1:-1]

process(entry_key, entry_type, entry)
