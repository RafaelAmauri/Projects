# Depends

rsync

## Usage

git clone https://github.com/RADA77777/Projects

cd "Projects/Backup Tool"

./backup $1, where $1 is the path to a folder.


## WARNING
 The parameter ($1) can be an absolute path (starting at /) or a relative path. You just CANNOT use ../path/to/dir or ../../path/to/dir.
You can use ./path/to/dir or just path/to/dir

## Description


This script makes delta updates (https://en.wikipedia.org/wiki/Delta_update) of a given directory and saves a tarball version to $HOME/Backups. It is possible to make a backup of any folder you want to. 

Making backups of very large folders (like /home) is not suggested, since they take a lot of space, even when compressed. After the backup is completed, the script will compress the files into a tarball (.tar.gz extension) and save it to $HOME/Backups to save as much space as possible.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please, make sure to test before committing

## License
[GPL 2.0](https://choosealicense.com/licenses/gpl-2.0/)
