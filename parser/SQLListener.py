# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#parse.
    def enterParse(self, ctx:SQLParser.ParseContext):
        pass

    # Exit a parse tree produced by SQLParser#parse.
    def exitParse(self, ctx:SQLParser.ParseContext):
        pass


    # Enter a parse tree produced by SQLParser#statement_list.
    def enterStatement_list(self, ctx:SQLParser.Statement_listContext):
        pass

    # Exit a parse tree produced by SQLParser#statement_list.
    def exitStatement_list(self, ctx:SQLParser.Statement_listContext):
        pass


    # Enter a parse tree produced by SQLParser#statement.
    def enterStatement(self, ctx:SQLParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLParser#statement.
    def exitStatement(self, ctx:SQLParser.StatementContext):
        pass


    # Enter a parse tree produced by SQLParser#create_index_statemnt.
    def enterCreate_index_statemnt(self, ctx:SQLParser.Create_index_statemntContext):
        pass

    # Exit a parse tree produced by SQLParser#create_index_statemnt.
    def exitCreate_index_statemnt(self, ctx:SQLParser.Create_index_statemntContext):
        pass


    # Enter a parse tree produced by SQLParser#select_statement.
    def enterSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#select_statement.
    def exitSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#result_column.
    def enterResult_column(self, ctx:SQLParser.Result_columnContext):
        pass

    # Exit a parse tree produced by SQLParser#result_column.
    def exitResult_column(self, ctx:SQLParser.Result_columnContext):
        pass


    # Enter a parse tree produced by SQLParser#table_name.
    def enterTable_name(self, ctx:SQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#table_name.
    def exitTable_name(self, ctx:SQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#ordering_term.
    def enterOrdering_term(self, ctx:SQLParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by SQLParser#ordering_term.
    def exitOrdering_term(self, ctx:SQLParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by SQLParser#column_alias.
    def enterColumn_alias(self, ctx:SQLParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by SQLParser#column_alias.
    def exitColumn_alias(self, ctx:SQLParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by SQLParser#database_name.
    def enterDatabase_name(self, ctx:SQLParser.Database_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#database_name.
    def exitDatabase_name(self, ctx:SQLParser.Database_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#index_name.
    def enterIndex_name(self, ctx:SQLParser.Index_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#index_name.
    def exitIndex_name(self, ctx:SQLParser.Index_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#indexed_column.
    def enterIndexed_column(self, ctx:SQLParser.Indexed_columnContext):
        pass

    # Exit a parse tree produced by SQLParser#indexed_column.
    def exitIndexed_column(self, ctx:SQLParser.Indexed_columnContext):
        pass


    # Enter a parse tree produced by SQLParser#column_name.
    def enterColumn_name(self, ctx:SQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#column_name.
    def exitColumn_name(self, ctx:SQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#table_alias.
    def enterTable_alias(self, ctx:SQLParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by SQLParser#table_alias.
    def exitTable_alias(self, ctx:SQLParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by SQLParser#name.
    def enterName(self, ctx:SQLParser.NameContext):
        pass

    # Exit a parse tree produced by SQLParser#name.
    def exitName(self, ctx:SQLParser.NameContext):
        pass


    # Enter a parse tree produced by SQLParser#expr.
    def enterExpr(self, ctx:SQLParser.ExprContext):
        pass

    # Exit a parse tree produced by SQLParser#expr.
    def exitExpr(self, ctx:SQLParser.ExprContext):
        pass


    # Enter a parse tree produced by SQLParser#literal_value.
    def enterLiteral_value(self, ctx:SQLParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by SQLParser#literal_value.
    def exitLiteral_value(self, ctx:SQLParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by SQLParser#keyword.
    def enterKeyword(self, ctx:SQLParser.KeywordContext):
        pass

    # Exit a parse tree produced by SQLParser#keyword.
    def exitKeyword(self, ctx:SQLParser.KeywordContext):
        pass


