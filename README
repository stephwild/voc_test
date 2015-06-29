# voc_test

Ask random question from a structured file (written in Python)

BNF of the structured file:

<voc_file> ::= <voc_item> <tail_voc_file>

<tail_voc_file> ::= "" | "\n" <tail_voc_file> |
                    <voc_item> <tail_voc_file>

<voc_item> ::= <entity> " - " <opt_whitespace> <list_entity>
               <opt_whitespace_return> <desc_item>
               <opt_whitespace_return> <ex_item>

<list_entity> ::= <entity> <opt_whitespace> "," <opt_whitespace> <list_entity>

<desc_item> ::= "\tDesc: " <definition>

<ex_item> ::= "\tEx: " <example>

<entity> ::= <name> <opt_whitespace> "[" <genre> "]" <opt_whitespace> "(" <comment> ")"

<opt_whitespace_return> ::= <opt_whitespace> "\n" | <opt_whitespace>

<opt_whitespace> ::= "\n " <opt_whitespace> | "\n\t" <opt_whitespace> |
                     " " <opt_whitespace> | "\t" <opt_whitespace" |
                     ""

<name> -> [:alnum:]
<genre> -> [:alnum:]
<comment> -> [:alnum:]

<definition> -> [:alnum:]
<example> -> [:alnum:]

A example will be:

fast-food [noun] (I love it) - restaurant [noun] (with bad food), resto [n.m] (fr: avec de la mauvaise nourriture)
	Desc: McDonald is a fast-food
	Ex: We will go to the fast-food
