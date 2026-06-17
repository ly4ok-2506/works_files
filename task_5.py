with open('resource/words.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

sorted_alphabetically = sorted(words)
sorted_by_length = sorted(words, key=len)
sorted_reverse = sorted(words, reverse=True)

with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_alphabetically))

with open('sorted_by_length.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_by_length))

with open('sorted_reverse.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted_reverse))

print("Готово")