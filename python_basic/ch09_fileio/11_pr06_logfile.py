with open("sample_logfile.txt") as f:
    content = f.read()

if "python" in content.lower():
    print(f"Is present")
else:
    print(f"Not present")
