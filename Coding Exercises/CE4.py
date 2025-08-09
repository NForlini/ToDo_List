filenames = ['doc1.txt', 'report1.txt', 'presentation1.txt']

for filename in filenames:
    file = open(f"../files/{filename}", "w")
    file.write("Hello")
    file.close()