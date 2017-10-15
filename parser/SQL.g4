/*

A simple SQL grammar for a very narrow subset of the language, for
demonstration purposes.

*/

grammar SQL;

parse : statement_list EOF ;

statement_list : statement ';' ( statement ';' )* ;

statement
  : create_index_statemnt
  | select_statement
  ;

create_index_statemnt
  : K_CREATE K_INDEX index_name K_ON table_name '(' indexed_column ')'
  ;

select_statement
  : K_SELECT ( K_DISTINCT )? result_column ( ',' result_column )*
    ( K_FROM ( table_name ( ',' table_name )* ) )?
    ( K_WHERE expr )?
    ( K_GROUP K_BY expr ( ',' expr )* ( K_HAVING expr )? )?
    ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
    ( K_LIMIT expr ( ( K_OFFSET | ',' ) expr )? )?
  ;

result_column
  : '*'
  | table_name '.' '*'
  | expr ( K_AS? column_alias )?
  ;

table_name
  : ( database_name '.' )? name ( K_AS? table_alias )?
  | name
  ;

ordering_term : expr ( K_ASC | K_DESC )? ;

column_alias : IDENTIFIER | STRING_LITERAL ;

database_name : name ;
index_name : name ;
indexed_column : name ;
column_name : name ;
table_alias : name ;

name
  : IDENTIFIER
  | keyword
  | STRING_LITERAL
  | '(' name ')'
  ;

expr
  : literal_value
  | ( ( database_name '.' )? table_name '.' )? column_name
  | '-' expr
  | expr ( '*' | '/' | '%' ) expr
  | expr ( '+' | '-' ) expr
  | expr ( '<' | '<=' | '>' | '>=' ) expr
  | expr ( '=' | '==' | '!=' | '<>' ) expr
  | expr K_AND expr
  | expr K_OR expr
  | '(' expr ')'
  ;

literal_value
  : NUMERIC_LITERAL
  | STRING_LITERAL
  ;

NUMERIC_LITERAL
  : [0-9]+ ( '.' [0-9]* )?
  ;

IDENTIFIER
  : '"' (~'"' | '""')* '"'
  ;

keyword
  : K_AND
  | K_AS
  | K_ASC
  | K_BY
  | K_COLUMN
  | K_CREATE
  | K_DESC
  | K_DISTINCT
  | K_FROM
  | K_GROUP
  | K_HAVING
  | K_IN
  | K_INDEX
  | K_LIMIT
  | K_OFFSET
  | K_ON
  | K_OR
  | K_ORDER
  | K_SELECT
  | K_TABLE
  | K_UNIQUE
  | K_WHERE
  | K_WITH
  ;

K_CREATE : C R E A T E ;
K_ON : O N ;
K_SELECT : S E L E C T ;
K_DISTINCT : D I S T I N C T ;
K_FROM : F R O M ;
K_WHERE : W H E R E ;
K_GROUP : G R O U P ;
K_BY : B Y ;
K_HAVING : H A V I N G ;
K_INDEX : I N D E X ;
K_ORDER : O R D E R ;
K_LIMIT : L I M I T ;
K_OFFSET : O F F S E T ;
K_AS : A S ;
K_ASC : A S C ;
K_DESC : D E S C ;
K_AND : A N D ;
K_OR : O R ;
K_COLUMN : C O L U M N ;
K_IN : I N ;
K_TABLE : T A B L E ;
K_UNIQUE : U N I Q U E ;
K_WITH : W I T H ;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];



SPACES
  : [ \u000B\t\r\n] -> channel(HIDDEN)
  ;
