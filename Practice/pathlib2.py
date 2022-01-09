from pathlib import Path
path=Path(".")
files=path.glob("*")
for file in files:
	print(file)
