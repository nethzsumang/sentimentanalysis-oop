###Sentiment Analysis for Python

System Requirements:
* Python 3.6.x

Running instructions:  
1. At the project root, open a command terminal.  
2. Run command `python index.py`  
  
Adding package dependency:  
1. From the project root, go to `/settings/`.  
2. Open `packages.json`.  
3. Write the package needed as follows:  
  
`"<package name in pip>": "<import name>"`  
  
Example:  
  
`"facebook-sdk": "facebook"`  
  
Hint:  
* You import `facebook-sdk` using the syntax: `import facebook`
* At default, `debug` is `false` in package checking. To enable
it, go to `index.py` and add the parameter `debug=True` in 
`check()` function call.
  