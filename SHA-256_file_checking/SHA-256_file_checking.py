import hashlib

def hash_file(file_path_1, file_path_2):
    """compute SHA-256 hashes of two files and return them"""
    def get_file_hash(file_path):
        """Helper function to computer SHA-256 hash of a single file."""
        hasher = hashlib.sha256()   # Use SHA-256 for better reliability
        try:
            with open(file_path,"rb") as file:
                while True:
                    chunk = file.read(8192) #8KB chunks for efficiency
                    if not chunk:
                        break
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {e}")

    # Compute hashes for both files
    hash1 = get_file_hash(file_path_1)
    hash2 = get_file_hash(file_path_2)
    return hash1,hash2

def compare_files(file_path1, file_path2):
    """Compares two files and print whether they are identical."""
    try:
        hash1, hash2 = hash_file(file_path1,file_path2)
        if hash1 == hash2:
            print(f"Files '{file_path1}' and '{file_path2}' are identical.")
        else:
            print(f"Files '{file_path1}' and '{file_path2}' are not identical.")
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    compare_files("pdf1.pdf","pdf2.pdf")