content = True
lineNum = 0
strFound = False
with open("sample_logfile.txt") as f:
    while content:
        content = f.readline()
        lineNum += 1
        if "python" in content.lower():
            strFound = True
            print(f"Is present on line number {lineNum}")
if not strFound:
    print(f"Not found")
