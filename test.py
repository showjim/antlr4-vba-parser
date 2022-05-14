import sys
import antlr4
from antlr4_vba_parser.vbaLexer import vbaLexer
from antlr4_vba_parser.vbaParser import vbaParser

if __name__ == '__main__':
    filename = "input.txt"
    input_stream = antlr4.FileStream(filename)
    # lexing
    lexer = vbaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    # # parsing
    # parser = vbaParser(stream)
    # tree = parser.startRule()

    # Parse all tokens until EOF
    stream.fill()

    tokenList = []
    tokenTypeList=[]
    for token in stream.tokens:
        tokenList.append(token.text)
        tokenTypeList.append(token.type)


    # Print tokens as text (EOF is stripped from the end)
    print(tokenList)
    print(tokenTypeList)