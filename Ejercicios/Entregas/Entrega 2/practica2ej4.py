from collections import Counter
evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""
#título: ok
#Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy difícil de leer: 2
titulo = evaluar.split('\n')[0].split()[1:]
#print(titulo)
cumple_titulo = len(titulo) <= 10
#print(cumple_titulo)
print('titulo: cumple\n' if cumple_titulo else 'titulo: no cumple\n')
# cada oración del resumen:
#hasta 12 palabras: fácil de leer
#entre 13-17 palabras: aceptable para leer
#entre 18-25 palabras: difícil de leer
#mas de 25 palabras: muy difícil 
cant_palabras = len(evaluar.split('\n')[1].split())
#print(cant_palabras)
if (cant_palabras < 13):
    print('facil de leer')
elif (cant_palabras > 12 and cant_palabras < 18):
    print('aceptable para leer')
elif (cant_palabras > 17 and cant_palabras < 26):
    print('dificil de leer')
else:    
    print('muy dificil')



