### TODO

#### Scripts
	1. move from assignment_groups too assignments
		- can include assignment_group info when requesting assignments?
	2. searching for item
	3. downloading assignment attachments
		- viewing assignment descriptions / downloading
	4. submitting assignments
    5. opening item in browser (if possible) (opening links)
	6. directories for assignments and courses, that can be used for downloading and submitting (in config)
	- [ ] preferring db or api request
			- [ ] per command (i.e. for get submission will check api request first)
			- [ ] on api request if different than db update db
	- [ ] submitting files
	- [ ] getting all submissions not just most recent (maybe optional)
	###### *Far out future*
		- [ ] graphql
		- [ ] support for instructors and admins side
#### Config
	- [ ] path for config file
	- [ ] auto gen course specific configs?
#### Database
	- [ ] sql array type using json.dumps/loads 
		- make it take sql type as param just for documentation of what types it is storing (maybe enforce as well by trying to cast items to python equivalent type)
	- [ ] online vs local requests?
	- [ ] storing local paths in db
	- [ ] easel mv for changing path of item
	- [ ] command to get item from name/id
			- [ ] flags limit search making it faster (put this in help message)
	- [ ] output db as tree structure 
			using simplified data from type
	- [ ] search for item
			- [ ] search with regex
	- [x] update courses merges with db instead of overwriting
			- [ ] give warning before overwrite
			- then for course in favorite courses call get_item for each item in course and merge with preexisting somehow?
#### optimize
	- [ ] verify efficiency of making db requests
	- [ ] async/threads for creating documents from items and writing them to db?
		- [ ] done in api module?
#### CLI interaction 
	**- [ ] Use python code or templates for output?**
			###assignments:
	- [ ] how to submit / choose assignment 
			- [ ] choosing assignment by search term (searches assignment name and attachment name)
	- [ ] choosing course for action 
			###general:
	- [ ] using flags in base to call parsers of subcommands like courses (using _get_parser...)
	- [ ] arguments for functions
	- [ ] how to display tree and select files to download (user prompt)
	- [ ] loading bars
	- [ ] provide ability to load functions in 
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
#### testing
	- [ ] all command tests
#### Documentation
	- [ ] make docs lol
	- [ ] how to test api/db requests? just fail when no internet/db?
#### General
	- [ ] scripts: 
		- [ ] ability to dynamically load plugins into cement (maybe use generate command)
		- [ ] run plugins as command
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
	- [ ] "watchdog" extension config option for when assignments get moved etc (daemon to watch files and update db)
