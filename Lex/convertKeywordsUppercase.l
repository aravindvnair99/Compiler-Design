%{
#include<stdio.h>
int i;
%}
keyword main|int|printf|include|for|void
%%

{keyword} {
for(i=0;i<yyleng;i++)
printf("%c",toupper(yytext[i]));
}
%%

main()
{
yyin=fopen("c.c","r");
yylex();
}

int yywrap()
{
return 1;
}
