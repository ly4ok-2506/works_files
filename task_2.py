def search_word_in_file():
    search_word = input("Введите слово: ").strip()

    found = False
    count = 0
    line_numbers = []

    with open('resource/text.txt', 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            cleaned_line = line.lower().translate(str.maketrans('', '', '.,!?;:"()'))
            words_in_line = cleaned_line.split()

            if search_word.lower() in words_in_line:
                found = True
                count += words_in_line.count(search_word.lower())
                line_numbers.append(idx)

    result_text = f"Слово '{search_word}':\n"
    result_text += f"Найдено: {'Да' if found else 'Нет'}\n"
    result_text += f"Встречается раз: {count}\n"
    result_text += f"Номера строк: {', '.join(map(str, line_numbers)) if line_numbers else '—'}\n"

    print(result_text)

    with open('search_results.txt', 'w', encoding='utf-8') as f:
        f.write(result_text)


if __name__ == "__main__":
    search_word_in_file()