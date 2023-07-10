# open data file in write mode

data = open('data/data.txt', 'r')

all_lines = data.readlines()

# get rid of note at bottom

del all_lines[66:68]

# get rid of newline character at the end of each row

clean = []

for x in all_lines:
    y = x.rstrip('\n')
    clean.append(y)

# turned tabbed txt file into usable python list

non_tab = []

for row in clean:
    x = row.split('\t')
    non_tab.append(x)

# get rid of reptitive/unecessary columns
# get rid of columns 1,2, and 4

for row in non_tab:
    del row[0]
    del row[0]
    del row[1]

# figure out row length for csv exporting

print(f'Number of Columns: {len(non_tab[0])}')

# remove uneccesary commas from column titles

col_titles = []

for x in non_tab[0]:
    y = x.replace(',', '')
    col_titles.append(y)

del non_tab[0]
non_tab.insert(0, col_titles)

# export list into csv file

row_counter = 0

with open('data/clean_data.csv', 'w') as f:
    for row in non_tab:
        for item in row:
            f.write(item + ',')

            # create rows every 52 values printed
            row_counter = row_counter + 1
            if row_counter % 52 == 0:
                f.write('\n')
