# Import modules

PIPE = "│"  
ELBOW = "└──"  
TEE = "├──"  
PIPE_PREFIX = "│   "  
SPACE_PREFIX = "    "

class DirectoryTreeGenerator:  
    def __init__(self, root_dir):  
        pass 
  
    def generate(self):  
        pass

class _TreeGenerator:  
    def __init__(self, root_dir):
        pass
  
    def build_tree(self):
        pass
  
    def _tree_head(self):
        pass
      
    def _tree_body(self, directory, prefix=""):
        pass
  
    def _add_directory(self, directory, index, entries_count, prefix, connector):
        pass
  
    def _add_file(self, file, prefix, connector):
        pass


if __name__ == '__main__':
    # Get the directory from user
    # Instantiate the DirectoryTreeGenerator class
    # and call generate method on it
    pass
