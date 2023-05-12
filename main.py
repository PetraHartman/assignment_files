import os
import zipfile


__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


"""
You need to master the following to complete this assignment:
- Importing and using Python modules;
- Reading and understanding Python standard library documentation.


Recently we found a super secret password to world domination.
We wrote it down in a text file but then we lost track of it in a
sea of text files. It must be somewhere in there...

Use Python's standard library to find the password.
After running the above wincpy start you should have the following files:

__init__.py (ignore this)
main.py
data.zip
In main.py, write the following functions:
"""


""" Goedgekeurd
1
clean_cache: takes no arguments and creates an empty folder named cache in
the current directory. If it already exists, it deletes everything in the
cache folder.

!!Danger!!
This function deals with deleting files. You should always be careful with
this! You should always do a dry run with print statements that to check if
everything is going according to plan before you commit to running the
script. We are not responsible if you mess up your system!

2
Cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments,
in that order. The function then unpacks the indicated zip file into a clean
cache folder.

You can test this with data.zip file."""


"""
3
cached_files: takes no arguments and returns a list of all the files in the
cache. The file paths should be specified in absolute terms. Search the web
for what this means! No folders should be included in the list. You do not
have to account for files within folders within the cache directory.


4
find_password: takes the list of file paths from cached_files as an argument.
This function should read the text in each one to see if the password is in
there. Surely there should be a word in there to indicate the presence of the
password? Once found, find_password should return this password string.
"""


def clean_cache():
    # Naam folder
    directory = "cache"
    # huidige pad (moet folder in komen te staan)
    parent_dir = os.getcwd()
    # pad folder
    path_directory = os.path.join(parent_dir, directory)
    # als folder al bestaat
    if os.path.exists(path_directory):
        # en als folder leeg is
        if len(os.listdir(path_directory)) == 0:
            print("exists and is empty")
        # anders  
        else:
            # voor elk bestand in folder
            for file in os.listdir(directory):
                # leeg folder
                os.remove(os.path.join(directory, file))
            print("exists and made empty")
    # anders
    else:
        # maak folder aan
        os.mkdir(path_directory)
        print("folder is formed")


def cache_zip(zip_file_path, cache_dir_path):
    # run clean_cache()
    clean_cache()
    # met zip_file_path als referentie
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        # plaats inhoud in zip_ref
        zip_ref.extractall(cache_dir_path)


def cached_files():
    # lege lijst
    file_list = []
    # path voor "cache"
    parent_path = os.getcwd()
    # "cache"
    file_dir_path = "cache"
    # absoluut path naar voor "cache"
    file_path_abs = os.path.abspath(os.path.join(parent_path, file_dir_path))
    # lijst van inhoud "cache"
    dir_list = os.listdir(file_path_abs)

    # aantal iteraties bij start
    loops = 0
    # max aantal iteraties om hele inhoud van "cache" te kunnen doorlopen
    max_loops = len(dir_list) + 1
    # terwijl de lengte van file_list ongelijk is aan de lengte van de dir_list
    while len(file_list) != len(dir_list):
        # als loops< max loops
        if loops < max_loops:
            # voor elke entry in dir_list
            for entry in dir_list:
                # als entry een file is
                if os.path.isfile(f"{file_path_abs}\{entry}") is True:
                    # entry als absoluut path toevoegen aan file_list
                    file_list.append(f"{file_path_abs}\{entry}")
        # als maximum aantal iteraties is bereikt
        if loops == max_loops:
            # stop
            break
    # geef file_list als resultaat
    return file_list


def find_password(file_list):
    # zoekterm
    searchword = "password"
    # voor elke file in file_list
    for file in file_list:
        # met open file als workfile
        with open(file) as workfile:
            # voor elke regel in workfile
            for line in workfile:
                # als het zoekword in de regel staat
                if searchword in line:
                    # splits de regel in woorden
                    split_line = line.split()
                    # als het zoekwoord niet in het woord staat
                    password = [x for x in split_line if searchword not in x]
    # zet password om naar string 
    password_string = " ".join([str(character) for character in password])
    # geef password weer
    return password_string


# print(clean_cache())
""" print(cache_zip("data.zip",
                "C://Users/Petra/Documents/Winc/Module_3/files/cache"))"""
# print(cached_files())

print(find_password(cached_files()))
