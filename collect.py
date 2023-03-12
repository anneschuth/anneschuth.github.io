import os
import subprocess
def proces(file):
    lines = {}
    content = []
    with open(file, 'r') as f:
        breaks = 0
        for line in f.readlines():
            if line.strip() == '---':
                breaks += 1
                continue
            if breaks == 1:
                k, v = [x.strip() for x in line.split(":", 1)]
                lines[k] = v
                continue
            if line.strip():
                content.append(line)



    print(f"Pdf {lines.get('pdf')}")
    print(f"Title {lines['title']}")
    print(f"Author {lines['author']}")
    print(f"Year {lines['year']}")
    print(f"Booktitle {lines.get('booktitle')}")
    print(f"Journal {lines.get('journal')}")

    asset = None
    pdffile = lines.get("pdf", '').strip('"')[1:]
    if os.path.exists(pdffile):
        asset = pdffile

    if not asset:
        in_file = input("Asset: ")
        if not in_file.endswith('.pdf'):
            in_file = in_file + '.pdf'
        asset = 'assets/' + in_file

    if os.path.exists(asset):

        if not content:
            print(f"Opening {asset}")
            os.system(f"open {asset}")
            content.append(input("Abstract: "))

        lines["pdf"] = '/' + asset
        with open(file, 'w') as f:
            f.write("---\n")
            for k, v in sorted(lines.items()):
                f.write(f"{k}: {v}\n")
            f.write("---\n\n")
            for l in content:
                f.write(l + "\n")




for filename in sorted(os.listdir("_publications")):
    proces(os.path.join("_publications", filename))