# split_file_by_key
Given a *SORTED* file, delimiter, and key(s), split the file into numerous out files based on the key(s).

## Requirements
A sorted file based on the same fields you want to split on. So if you want to split on the 7th field in a file, please ensure the file is sorted on that field otherwise you *will lose some of your data.*

#### Example: sort in file
```cat in_file.tsv | sort -k7 > sorted_in_file.tsv```

#### Example: verify number of lines in each out file is same as in the in file
```cat sorted_in_file.tsv | cut -f 7 | uniq -c```

## Usage
```
./split_file_by_key.py --help
usage: split_file_by_key.py [-h] [--fields FIELDS] [--delimiter DELIMITER]
                            [--line-terminator LINE_TERMINATOR]
                            in_file

Given a *SORTED* file, delimiter, and key(s), split the file into numerous out
files based on the key(s).

positional arguments:
  in_file               Path to input file

optional arguments:
  -h, --help            show this help message and exit
  --fields FIELDS       Field number, comma separated starting at 1 (e.g. "6",
                        "6,7", etc)
  --delimiter DELIMITER
                        Delimiter (e.g. "\t", ",", etc)
  --line-terminator LINE_TERMINATOR
                        line terminator (e.g. "\n", "\r\n", etc)
```

## Example Command
```
./split_file_by_key.py sample.tsv --fields 1 
```

## Example Input (in File)
```
1	foo	bar
1	baz	qux
2	cookies	are
2	too	delicious
2	must	stop
2	but	can't
3	too	delicious
3	needing	milk
```

## Example Output
```
# filename: sample.tsv.1.split
1	foo	bar
1	baz	qux
# filename: sample.tsv.2.split
2	cookies	are
2	too	delicious
2	must	stop
2	but	can't
# filename: sample.tsv.3.split
3	too	delicious
3	needing	milk
```
