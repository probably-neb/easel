Options for how to structure database

1. Separate tables
	pros:
		- benefits of flat structure with much faster search
		- must use nested (table) searches -> per type searches
				- need some way to store types
				- use default for list of types, course ids, user info, list of course names? (just often used info)
		- no db.all()
				- but can store types in _default and retrieve easily
		- small returned documents
		- store with doc ids

2. flat: all items same depth
	pros:
		- db.all() to go through all
		- no managing Query.page,module,file etc just check fragement {"type":type, "data": data}
		- smaller return documents -> easier to work with when returned
		- use doc_ids as primary form of accessing things, 
	cons:
		- search everything every time
		- non human readable
		- long write time because must serialize each item individually (I think)

3. as course
	pros:
		- logical tree structure -> human readable
		- less serialization/search
	cons:
		- highly complicated nested query
		- big query returns -> searching returned documents again (i.e. Query assignment group by name then assignment group must be retrieved from returned doc)

# shouldn't do, will return entire document including everything of same type meaning will have to search again
4. nested by type
	pros:
		- benefits of flat structure with much faster search
		- must use nested searches

