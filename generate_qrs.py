import uuid
import csv

# Generate a CSV with num_codes UUIDs in the proper format
num_codes = input("How many codes? ")
num_files = input("How many files? ")
fileprefix = input("File name? ")
print("")

def writeUUIDs(filename, n):
    uuids = [uuid.uuid4() for _ in range(int(n))]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["qr_code", "link"])
        for id in uuids:
            writer.writerow([str(id), "https://racquetpass.com/your-racquet/" + str(id)])

i = 1
for file in range(int(num_files)):
    writeUUIDs(fileprefix + str(i) + ".csv", num_codes)
    i += 1
