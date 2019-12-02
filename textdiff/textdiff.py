#!/usr/bin/python
# find the difference between two texts
# tested with Python24   vegaseat  6/2/2005
import difflib


def main():
    text1 = open("C:/Users/j.zhang/PycharmProjects/python_samples/textdiff/test.txt","r").read()
    text2 = open("C:/Users/j.zhang/PycharmProjects/python_samples/textdiff/filter.txt","r").read()
    print '-'*50

    # create a list of lines in text1
    text1Lines = text1.splitlines(1)
    text2Lines = text2.splitlines(1)

    diffInstance = difflib.Differ()
    diffList = list(diffInstance.compare(text1Lines, text2Lines))
    print '-'*50
    print "Lines different in text1 from text2:"
    for line in diffList:
      if line[0] == '-':
        print line,

    print "Lines different in text2 from text1:"
    diffList = list(diffInstance.compare(text2Lines, text1Lines))
    for line in diffList:
      if line[0] == '-':
        print line,


if __name__ == "__main__":
    main()

