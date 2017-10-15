import sys

from antlr4 import CommonTokenStream, FileStream

from SQLLexer import SQLLexer
from SQLParser import SQLParser


def main(argv):
    lexer = SQLLexer(FileStream(argv[1]))
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    tree = parser.parse()
    print(tree.toStringTree())


if __name__ == '__main__':
    main(sys.argv)
