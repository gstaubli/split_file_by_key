# split_file_by_key
Given a *SORTED* file, delimiter, and key(s), split the file into numerous out files based on the key(s).

## Requirements
A sorted file based on the same fields you want to split on. So if you want to split on the 7th field in a file, please ensure the file is sorted on that field otherwise you *will lose some of your data.*

#### Example: sort in file
```cat in_file.tsv | sort -k7 > sorted_in_file.tsv```

#### Example: verify number of lines in each out file is same as in the in file
```cat sorted_in_file.tsv | cut -f 7 | uniq -c```
