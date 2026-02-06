# Richard Perez

import sys

class Cleaned:
    def __init__(self, filename = "any"):
        self.filename = filename
        self.data = self.read_file()

    # reading the file
    def read_file(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()

        data = []
        key = None
        cur = ""

        for line in lines:
            line = line.strip()
            # skiping our empty lines
            if not line:
                continue
            if '=' in line:
                if key and cur:
                    data.append((key, cur))
                parts = line.split('=')
                key = parts[0].strip()
                # working around the ""
                cur = parts[1].strip().replace("“", "").replace("”", "").replace("‘", "").replace("’", "").strip("[]")
            else:
                cur += line.replace("“", "").replace("”", "").replace("‘", "").replace("’", "").strip("[]")
        if key and cur:
            data.append((key, cur))
        tidy_data = []
        for i in range(0, len(data), 2):
            # concatinating the string here 
            str = data[i][1]
            words = data[i + 1][1].split(', ') if ', ' in data[i + 1][1] else data[i + 1][1].split()
            tidy_data.append((str, words))

        return tidy_data

def targets(str, words):
    stored = []
    for word in words:
        index = str.find(word)
        if index != -1:
            stored.append((index, word))

    stored.sort()
    # getting the words and indexes from stored 
    indexes = [idx for idx, _ in stored]
    words = [word for _, word in stored]
    
    return indexes, words

def main():
    filename = sys.argv[1]
    processor = Cleaned(filename)
    # printing the output 
    for i, (a, b) in enumerate(processor.data, start=1):
        indexes, words = targets(a, b)
        print(f"Array number {i}:")
        print("Indexes:", indexes)
        print("Target words:", words)
        print()

if __name__ == "__main__":
    main()