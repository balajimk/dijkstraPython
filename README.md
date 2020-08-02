# dijkstraPython
Coding Dijkstra's shortest path in Python.

The code uses py_linq from https://viralogic.github.io/py-enumerable/.

You can learn the Dijkstra's algorithm from https://www.youtube.com/watch?v=pVfj6mxhdMw

## Changes to the generally accepted logic
- Instead of visited & unvisited vertices list, I have used visited flag in the Vertex class.
- Using used flag on Edge class to be sure that the edge has been used to calculate the distance already though this is not mandatory.

## How to run the code
Clone or download the code from this repository.
Open the folder in Visual Studio code or your preferred text editor.
Install py-linq by running the command in the prompt / terminal"
> pip install py-linq

and to execute the code:
> {full path to  python}/python.exe {full path to the folder}/dijkstraClient.py

This is my first try with Python and so, bear with the issues :)
