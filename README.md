# split_file_by_key
Given a file, delimiter, and key(s), split the file into numerous out files based on the key(s).

## Usage
```
./split_file_by_key.py --help
usage: split_file_by_key.py [-h] [--fields FIELDS] [--delimiter DELIMITER]
                            [--line-terminator LINE_TERMINATOR]
                            in_file

Given a file, delimiter, and key(s), split the file into numerous out
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
