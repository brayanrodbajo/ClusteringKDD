from os import listdir 
from math import log
def leer (directorio) :
	arr = [doc for doc in listdir(directorio)]
	return arr
	
def matriz_ocurrencias (documentos, palabras) :
	matriz = []
	for doc in documentos: 
		print (doc)
		archivo = open(directorio + doc, "r") 
		ocurrencias = 0
		fila = [0 for c in range (len(palabras))]
		index =0
		for linea in archivo.readlines():
			cont = 0
			for palabra in palabras:
				fila[cont] += linea.count(palabra)
				cont +=1
		matriz.append(fila)	
		print (fila)
	return matriz	
	


#maxi : Numero de veces que aparece en el documento que mas esta la palabra i.
#~ arreglo del tamano del numero de palabras  
#ni: arreglo del tamano del numero de palabras
def matriz_similitud (matriz, N,n_palabras) :
	print "\n"
	maxs = [ ]
	Ni = []
	#~ maxs = matriz[:][0:] 
	for i in range(n_palabras):
		columna =[matriz[pal][i] for pal in range(N)]
		maxs.append(max(columna))
		Ni.append (len ([i for i, e in enumerate(columna) if e != 0]))
	print "maxs"
	print maxs
	print "\n"
	print "Ni"
	print Ni
	print "\n"
	for i in range (len (matriz)):
		for j in range (len (matriz [i])):
			try:
				matriz [i] [j] = float ( float ((matriz [i] [j] /( float ((matriz [i] [j]) * maxs[j])))) * float (log (N/float (Ni[j]),10)))
				print float (log (N/float (Ni[j]),10))
				
			except Exception:
				 matriz [i] [j] = "0"
	print matriz		 
		
#~ print (matriz)
directorio = "preprocesados/"
palabras = ["colombi", "petr", "procur", "nacion", "bogot", "mineri", "dat", "clust", "clasificacion", "min", "mining", "futbol", "jugador", "mundial", "falca", "messi", "fif", "fifa", "cop"]	
documentos = leer (directorio)
matriz = matriz_ocurrencias (documentos,palabras)
matriz_similitud (matriz,len(documentos),len(palabras))

			 
		
	
	


