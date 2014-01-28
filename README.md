# Sublime Text Fill CF Query

A Sublime Text plugin that takes query statements in ColdFusion debug output
and fills in CFQUERYPARAMs.

## Example
As an example let's say you have a query in your ColdFusion page that outputs
debug info that looks like this.

```sql
SELECT
	someId
FROM someTable
WHERE
	someTable.a > ?
	AND someTable.active=1
	AND someTable.noteTypeName IN (?,?)

Query Parameter Value(s) -
Parameter #1(cf_sql_varchar) = 10
Parameter #2(cf_sql_varchar) = Bob
Parameter #3(cf_sql_varchar) = Joe
```

Notice that each parameter in the query is represented by a question mark. Also
note that the actual parameter values are below the query. Don't you want the
parameters to be filled into your query?

If you have this plugin installed you can copy the query and parameters into
Sublime, select the text and press *CTRL + ALT + F* and the parameters will be
magically filled into the question marks. Ta da!

```sql
SELECT
	someId
FROM someTable
WHERE
	someTable.a > '10'
	AND someTable.active=1
	AND someTable.noteTypeName IN ('Bob','Jo')
```

## Change History
* 01/28/2014:
   * Selected text with no line feed at the end was causing the last character to be cut off. This has been addressed. #1
   * Addressed a Python 3/Sublime Text 3 compatability issue. #2

## License
The MIT License (MIT)
Copyright (c) 2013 Adam Presley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.