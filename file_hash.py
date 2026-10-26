import hashlib
def file_hash(filenm):
    sha256 = hashlib.sha256()
    with open(filenm, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

filenm = file_hash("Demo.txt")
print("Hash of file : ",filenm)