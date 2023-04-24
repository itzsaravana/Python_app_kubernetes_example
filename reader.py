import csv
import time
import shutil


def main():
    csv_list = read_csv_file()
    file_lenth= len(csv_list)
    if file_lenth > 0:
        write_txt_file(csv_list)
    print("file size - ", file_lenth)
    time.sleep(10)


def write_txt_file(csv_list):
    file1 = open("data/output.txt", "a")
    i = 0
    # write mode
    for lines in csv_list:
        file1.write(lines + '\n')
        i = i + 1
        print('file processing...')
        time.sleep(10)
    file1.close()
    if len(csv_list) == i:
        try:
            shutil.move('data/test.csv', 'processed_file/')
            print('file moved')
        except Exception:
            print("File can't be moved")

def read_csv_file():
    # opening the CSV file
    mylist = []
    try:
        with open('data/test.csv', mode='r') as file:
            # reading the CSV file
            csvfile = file.readlines()
            for lines in csvfile:
                mylist.append(lines)
    except Exception:
        print("File not Available")

    return mylist


if __name__ == "__main__":
    print("starting point")
    while True:
        main()
