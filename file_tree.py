PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

#credit to article written by Leodanis Pozo Ramos for Real Python [https://realpython.com/directory-tree-generator-python/]
#class CanvasFile:
#    def __init__(self, name, is_file, id=None, parent=None):
#        self.name = name
#        self.is_file = is_file
#        self.parent = parent
#        self.id = id
#        if not self.is_file:
#            self.children = []
#        self._tree = []

#    def add_children(self, files: list):
#        for file in files:
#            if not self.is_file:
#                if not isinstance(file, CanvasFile):
#                    #TODO: how to initialize children as canvasFiles with correct is_file bool
#                    file = CanvasFile(file, True)
#                self.children.append(file)
#                file.add_parent(self)

#    def add_parent(self, file):
#        self.parent = file

#    def build_tree(self):
#            self._tree_head()
#            self._tree_body(self)
#            return self._tree

#    def _tree_head(self):
#        self._tree.append(f"{self.parent}/")
#        self._tree.append(PIPE)

#    def _tree_body(self, canfile, prefix=""):
#            entries = canfile.children
#            entries = sorted(entries, key=lambda entry: entry.is_file)
#            entries_count = len(entries)
#            for index, entry in enumerate(entries):
#                connector = ELBOW if index == entries_count - 1 else TEE
#                if not entry.is_file:
#                    self._add_directory(
#                        entry, index, entries_count, prefix, connector
#                    )
#                else:
#                    self._add_file(entry, prefix, connector)

#    def _add_directory(self, canfile, index, entries_count, prefix, connector):
#            self._tree.append(f"{prefix}{connector} {canfile.name}/")
#            if index != entries_count - 1:
#                prefix += PIPE_PREFIX
#            else:
#                prefix += SPACE_PREFIX
#            self._tree_body(
#                canfile=canfile,
#                prefix=prefix,
#            )
#            self._tree.append(prefix.rstrip())

#    def _add_file(self, file, prefix, connector):
#            self._tree.append(f"{prefix}{connector} {file.name}")
