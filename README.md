sutin
======

Hassle-free scaffold generation engine. Use it to very quickly create experimental environments.

**Install:**  `pip3 install git+https://github.com/keynmol/joe_docker.git`

**Example:**  `sutin scala hello-scala` will create a minimal SBT scala project in `hello-scala/`

Available templates: `r`, `r-package`, `scala`, `spark`.

```
usage: sutin [-h] [-f] template [folder]

positional arguments:
  template     select a template for your new project
  folder       folder in which to create the project

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  force create project even if the folder is not empty
```