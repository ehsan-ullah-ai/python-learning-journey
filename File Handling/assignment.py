def count_text_file(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    # word_count = sum(len(line.split()) for line in lines)
    
    
    word_count = 0
    for line in lines:
      word_in_line = line.split() # split() --> split the line into words
      word_count += len(word_in_line)
    
    # char_count = sum(len(line) for line in lines)
    char_count = 0;
    for line in lines:
      char_count += len(line)
    return line_count, word_count, char_count

file_path = "File Handling/source.txt"

line_count, word_count, char_count = count_text_file(file_path)

print(f"Lines: {line_count}\nWords: {word_count}\nCharacter: {char_count}")


