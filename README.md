# FrameQL
## Overview
FrameQL is a Declearative language that takes SQL-ish language to perform video analytic

## Structure of FrameQL language
A valid FrameQL program is a ***frameQLstatements***.
*frameQL statements* will consists of multiple ***frameQL statement***.
Each ***frameQLstatement*** can be either ***ddlStatement*** or ***dmlStatement***, *** transactionStatement***
Since FrameQL will be used mainly for video exploratory purpose, we will focus on ***dmlStatement***, specifically, ***selectStatement***.

A ***selectStatement*** will contain ***querySpecification*** that starts with **SELECT**.

Each ***querySepcification*** will take the form of of:
```
     SELECT ***selectSpec*** ***selectElements***
    ***fromClause***  ***errorTolerenceExpression*** ***confLevelExpression***
```

Where ***selectSpec*** can be empty or **DISTINCT**.

***selectElements*** is a list of attribltes from the table returned in ***fromClause***

***fromClause*** will take the form of
```
FROM tableSources WHERE (expressions)
```




# Grammar for frameQL
We built a grammar using ANTLR


## How to compile
### Use ANTLR4 to construct the parser and the lexer

```
antlr4 -Dlanguage=Python3 *.g4 -o ../build
```

### Compile all java files in build
Go to ../build and execute:
```

```

###
## How to construct parse tree
in build, run:
```
grun frameQL root -gui
```
It will ask for inputs in the command prompt

Or we can provide input txt file via:
```
grun frameQL root -gui query.txt
```

In the end, grun will output the parse tree

## Problems
### No runtime environemnt
Just export CLASSPATH 	
```
export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
```
