evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing 
resources provides the promise of capturing unprecedented details of 
large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

separar = evaluar.split ("resumen:")
titulo = separar[0].split(" ")
cant = 0
for palabra in titulo:
    cant = cant + 1
if cant <= 10:
    tit = True

dicci = {"facil de leer": 0,
         "aceptable": 0,
         "dificil": 0,
         "muy dificil": 0
         }

oraciones = separar[1].split (".")

for oracion in oraciones:
    palabras = oracion.split(" ")
    cant = 0
    for pal in palabras:
        cant = cant + 1
    match cant:
        case cant if cant <= 12:
            dicci["facil de leer"] = dicci["facil de leer"] + 1
        case cant if (cant >= 13) & (cant <= 17):
            dicci["aceptable"] = dicci["aceptable"] + 1
        case cant if (cant >= 18) & (cant <= 25):
            dicci["dificil"] = dicci["dificil"] + 1
        case cant if (cant > 25):
            dicci["muy dificil"] = dicci["muy dificil"] + 1

print (dicci)
        