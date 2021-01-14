#!/usr/bin/env python
import sys

from tfidf.sayhello import say_hello
from tfidf.starter import main as tfidf_starter


def main():
    say_hello()
    print("this is program about TF-IDF")
    tfidf_starter(sys.argv[1:])


if __name__ == '__main__':
    main()
