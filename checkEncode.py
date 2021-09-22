
import chardet
import glob
import sys
import pprint


def get_file_encoding(src_file_path):
    """
    Get the encoding type of a file
    :param src_file_path: file path
    :return: str - file encoding type
    """

    with open(src_file_path) as src_file:
        return src_file.encoding
    

def calculate_line_endings(path):
    # order matters!
    endings = [
        b'\r\n', #crlf
        b'\n\r', #lfcr
        b'\n', #cr
        b'\r', #lf
    ]
    counts = dict.fromkeys(endings, 0)

    with open(path, 'rb') as fp:
        for line in fp:
            for x in endings:
                if line.endswith(x):
                    counts[x] += 1
                    break
    return(counts)

           

def get_file_encoding_chardet(file_path):
    """
    Get the encoding of a file using chardet package
    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as f:

        result = chardet.detect(f.read())
        return result['encoding']


def search_file():
        # All files ending with .txt
    return(glob.glob('C:\\Users\\20100907\\Documents\\python\\*.txt')) 
    # All files ending with .txt with depth of 2 folder
    #print(glob.glob("/home/adam/*/*.txt")) 


def printDict(value):
   pprint.pprint(value, width=1)

def main():
    file_path =  search_file()
    for file in file_path: 
        print(str(file))
        printDict(calculate_line_endings(file))
        print('Endcoding ' + str(get_file_encoding(file)))
        print('Endcoding with chardet: ' + str(get_file_encoding_chardet(file)))

#search_file("toto")
main()