#!/usr/local/bin/io
run
    1. #!/usr/local/bin/io
    1. io xxx.io

feature
    dynamic prototype-based programming language
    消息反射
    对象反射
    concurrency, coroutines, actors, and futures

::=  Creates slot, creates setter, assigns value
:=   Creates slot, assigns value
=    Assigns value to slot if it exists, otherwise raises exception

exp        ::= { message | terminator }
message    ::= symbol [arguments]
arguments  ::= "(" [exp [ { "," exp } ]] ")"
symbol     ::= identifier | number | string
terminator ::= "\n" | ";"
