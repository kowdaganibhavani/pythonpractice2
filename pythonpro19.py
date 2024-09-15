import filecmp
import hashlib

def are_pdfs_identical(file1, file2):
   
    result = filecmp.cmp(file1, file2, shallow=False)
    
    if result:
        print("The PDF files are identical.")
    else:
        print("The PDF files are different.")


if __name__ == "__main__":
    pdf1 = "file1.pdf"
    pdf2 = "file2.pdf"
    are_pdfs_identical(pdf1, pdf2)


def hash_file(file_path):

    hasher = hashlib.md5()
    
    with open(file_path, 'rb') as f:
  
        while chunk := f.read(8192):
            hasher.update(chunk)
    
    
    return hasher.hexdigest()

def are_pdfs_identical(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if hash1 == hash2:
        print("The PDF files are identical.")
    else:
        print("The PDF files are different.")

if __name__ == "__main__":
    pdf1 = "file1.pdf"
    pdf2 = "file2.pdf"
    are_pdfs_identical(pdf1, pdf2)
