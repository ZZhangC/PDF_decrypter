# -*- coding: utf-8 -*-
import sys, os, pikepdf

def unlock_file(file):
	pdf = pikepdf.open(file, allow_overwriting_input=True)
	pdf.save(file.split('.')[0] + '_decrypted.pdf')


def unlock_directory(folder = './'):
	os.chdir(folder)
	filelist = os.listdir()
	for file in filelist:
		if os.path.splitext(file)[1] == '.pdf':
			unlock_file(file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            else:
                if os.path.isdir(i):
                    unlock_directory(i)
                else:
                    unlock_file(i)
    else:
        print('No files inputed!')