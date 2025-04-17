'''
🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
  Read the contents of input.txt.
  Count the number of words in the file.
  Convert all text to uppercase.
  Write the processed text and the word count to a new file called output.txt.
  Print a success message once the new file is created.
'''

with open('input.txt', 'w') as f:
  f.write("this is the first line")
  f.write("this is the second line")
  f.write("this is the third line")
  f.write("this is the forth line")
  f.write("this is the fifth line")

with open('input.txt', 'r'):
  content = f.read()

# for word count
word_count = len(content.split())

# for uppercase conversion
uppercase_content  = content.upper()

with open('output.txt', 'w') as f:
  f.write(uppercase_content)
  f.write(f"the word count is: {word_count}")

print("congratulation writing and conversion done")
  
