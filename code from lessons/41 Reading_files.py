# Fayllar: faylların oxunması
# stream

file_stream = open('folder/file.txt', 'r')

print(f" Read from: {file_stream.tell()}")
print(file_stream.readline())
print(file_stream.seek(0))
print(f" Read from: {file_stream.tell()}")
print(file_stream.readline())
print(f" Read from: {file_stream.tell()}")

file_stream.close()
