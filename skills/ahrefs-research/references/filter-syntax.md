
# Filter syntax

Some API endpoints accept a `where` parameter, which applies a filter to the result set.

The following sections give some examples of filter usage and a full syntax reference.

## Examples


> For more real world examples, try applying some filters to a report on ahrefs.com using our visual interface, and then press the `API {}` button to view the `where` parameter of the generated API v3 query.


Field "foo" equals 3:

```json
{ "field": "foo", "is": ["eq", 3] }
```

For fields of type object, use dot notation to refer to nested fields. Field "bar", nested under field "foo", equals 3:

```json
{ "field": "foo.bar", "is": ["eq", 3] }
```

The integer field "foo" equals 3 and the integer field "bar" is less than 10:

```json
{
    "and": [
        { "field": "foo", "is": ["eq", 3] },
        { "field": "bar", "is": ["lt", 10] }
    ]
}
```

Either the uppercased value of the string field "foo" equals "AHREFS", or all string elements in the array field "bar" have the prefix "Ahrefs" and suffix "seo".

```json
{
  "or": [
    {
      "field": "foo",
      "modifier": "uppercase",
      "is": ["eq", "AHREFS"]
    },
    {
      "field": "bar",
      "list_is": {
        "and": [
          ["prefix", "Ahrefs"],
          ["suffix", "seo"],
        ]
      }
    }
  ]
}
```

## Language reference

The filter syntax is described by the following grammar, expressed in [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)-style notation. 

A term enclosed in angle brackets `<` and `>` denotes a symbol.  A symbol followed by a `+` denotes a non-empty array containing the symbol. A `?` preceding an object field indicates that the field is optional.

The two terminal symbols are defined as follows:

- `<field_alias>` A filter field alias. See the particular endpoint's documentation for the list of valid aliases. Note that the `select` and `where` parameters may accept different aliases.
- `<value>` A JSON value. It should match the type of the field (or of the field's modifier, if one is present).

Permitted patterns in regex filter expressions differs by tool.
- Keywords Explorer: Only `*` as a wildcard operator.
- Site Explorer: [RE2](https://github.com/google/re2/wiki/Syntax) syntax.

```json
<bool_filter> ::= { "and" : <bool_filter>+ }
              |   { "or" : <bool_filter>+ }
              |   { "not" : <bool_filter> }
              |   <expr>

<expr> ::= {
             "field" : <field_alias>,
             ? "is": <condition>,
             ? "list_is": <list_condition>
           }

<condition> ::= [ "eq", <value> ]
            |   [ "neq", <value> ]
            |   [ "gt", <value> ]
            |   [ "gte", <value> ]
            |   [ "lt", <value> ]
            |   [ "lte", <value> ]
            |   [ "substring", <value> ]
            |   [ "isubstring", <value> ]
            |   [ "phrase_match", <value> ]
            |   [ "iphrase_match", <value> ]
            |   [ "prefix", <value> ]
            |   [ "suffix", <value> ]
            |   [ "regex", <value> ]
            |   "empty"
            |   "is_null"

<condition_bool_filter> ::= { "and" : <condition_bool_filter>+ }
                        |   { "or" : <condition_bool_filter>+ }
                        |   { "not" : <condition_bool_filter> }
                        |   <condition>

<list_condition> ::= { "any" : <condition_bool_filter> }
                 |   { "all" : <condition_bool_filter> }
```


