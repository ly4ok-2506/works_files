files = ['file1.txt', 'file2.txt', 'file3.txt']

result = open('combined.txt', 'w', encoding='utf-8')

for name in files:
    file_path = 'resource/' + name

    f = open(file_path, 'r', encoding='utf-8')
    content = f.read()
    f.close()

    result.write(f"=== Содержимое {name} ===\n")
    result.write(content)
    result.write('\n\n')

result.close()
print("Файлы объединены")