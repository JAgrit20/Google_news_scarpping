import os
import pandas as pd

def get_file_content_and_filenames(folder_path, max_files=200):
    content_list = []
    filenames_list = []
    skipped_files = 0
    processed_files = 0

    for filename in os.listdir(folder_path):
        if processed_files >= max_files:
            break

        if filename.endswith(".txt"):
            try:
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                    content = file.read().replace('\n', ' ').replace('\r', ' ')
                    content_list.append(content)
                    filenames_list.append(filename)
                    processed_files += 1
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
                skipped_files += 1

    return content_list, filenames_list, skipped_files

folder_path = "cases"
content, filenames, skipped_files_count = get_file_content_and_filenames(folder_path)

# create a DataFrame from the content and filenames
df = pd.DataFrame({'filename': filenames, 'content': content})

# save the DataFrame to a CSV file
df.to_csv('cases_content_final.csv', index=False, encoding='utf-8')

print(f"Number of files skipped: {skipped_files_count}")
