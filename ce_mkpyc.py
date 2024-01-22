import re, glob, py_compile

flist = []
base_path = "build/lib/python3.10/"

srcfiles = [*glob.glob(base_path + "**", recursive=True)]

for py in srcfiles:
    if py.endswith(".py") and not py.startswith(base_path + "test/") and not py.startswith(base_path + "lib2to3/"):
        try:
            py_compile.compile(py, py+"c", optimize=1, doraise=True)
        except:
            flist.append(py[len(base_path):])
        else:
            flist.append(py[len(base_path):] + "c")
    elif "__pycache__" not in py and not py.endswith(".pyc"):
        flist.append(py[len(base_path):])


with open("zip.list", mode="w") as f:
    f.write("\n".join(flist))
