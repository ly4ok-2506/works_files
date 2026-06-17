file = open('resource/input.txt', 'r', encoding='utf-8')

lines = file.readlines()
file.close()

line_count = len(lines)

word_count = 0

for line in lines:
    words = line.split()

    word_count = word_count + len(words)

output_file = open('statistics.txt', 'w', encoding='utf-8')

output_file.write('Количество строк: ' + str(line_count) + '\n')
output_file.write('Количество слов: ' + str(word_count) + '\n')

output_file.close()

print('Результаты сохранены в файл statistics.txt')
print('Строк:', line_count)
print('Слов:', word_count)