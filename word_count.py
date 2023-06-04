import os

folder_path = "C:/Users/jagri/OneDrive/Desktop/Scapping_code/Google_news_scarpping-/cases"  # replace with the path to your folder

total_words = 0
num_files = 0
max_words = 0
min_words = float("inf")
skipped_files = 0
count = 0

# iterate over all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r") as file:
                contents = file.read()
                words = contents.split()
                num_words = len(words)
                total_words += num_words
                num_files += 1
                if num_words <3000:
                    count = count +1

                if num_words > max_words:
                    max_words = num_words
                if num_words < min_words:
                    min_words = num_words
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            skipped_files += 1

# calculate the average number of words per file
if num_files > 0:
    avg_words = total_words / num_files
else:
    avg_words = 0

# print the results
print(f"Total words: {total_words}")
print(f"Number of files: {num_files}")
print(f"Number of skipped files: {skipped_files}")
print(f"Average words per file: {avg_words}")
print(f"Maximum words in a file: {max_words}")
print(f"Minimum words in a file: {min_words}")
print(f"Minimum words in a file: {count}")
