<img src="./images/directory-tree-generator.png" width="700"/>

# Directory Tree Generator
> DIFFICULTY: **EASY**

In this project you build a command-line tool to list the contents of a directory or folder in a tree-like diagram with **pathlib** module. There are various solutions available to achieve this task, such as the *tree* command, which is available on most operating systems. There are also several tools available such as *treelib*, *dirtriex*, and so on. However, we will create our own solution to get a better understanding.

Our directory tree generator will have a user-friendly command line interface (CLI). It also comes with unique features, such as displaying a tree diagram with the contents of a directory on our terminal.

The tree diagram contains following components:
- **Head**:  provide the root directory representation
- **Body**: give the directory content representation.

The tree body representation will have the name of the root directory and an additional pipe (|) character to connect the tree and body.  
The combined directory tree structure will look like as below:

<img src="./images/directory-tree-generator-diagram.png" width="500"/>


## TODO

1. Define variables, PIPE, ELBOW and TEE. These variables contain string characters '│', '└──' and '├──' respectively.
2. Write the high-level *DirectoryTreeGenerator* class to generate and display the tree diagram. This class have a *generate()* method that is responsible for generating and displaying the directory tree diagram.
3. Write a low-level *_TreeGenerator* class to traverse the directory structure and build the list of entries that will form the tree diagram. This class have a *build_tree()* method to perform this operation.
4. Get the directory from user. Instantiate the DirectoryTreeGenerator class and call generate method on it.
