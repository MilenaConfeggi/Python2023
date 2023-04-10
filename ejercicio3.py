import string

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
""".lower()

  


palabras = jupyter_info.split(" ")
letra = input("ingrese letra a buscar ")
if  not letra.isalpha():
    print ("el caracter ingresado no es una letra")
else:
  for palabra in palabras:
      if palabra.startswith(letra):
          print (palabra)
