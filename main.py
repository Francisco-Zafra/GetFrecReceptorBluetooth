import urllib.request
from numpy import arange
from numpy import sort
from numpy import array
from numpy import ndarray

def Diff(a, b):
    r = []
    if len(a) >= len (b):
        aa = a
        bb = b
    else:
        aa = b
        bb = a

    for e1 in aa:
        esta = False
        for e2 in bb:
            if(e1 == e2):
                esta = True
        if not esta:
            r.append(e1);

    return r

def Eq(a,b):
    r = []
    if len(a) >= len (b):
        aa = a
        bb = b
    else:
        aa = b
        bb = a

    for e1 in aa:
        esta = False
        for e2 in bb:
            if(e1 == e2):
                esta = True
        if esta:
            r.append(e1);

    return r

def getFrecOcupadas(url):
    fp = urllib.request.urlopen(url)

    mybytes = fp.readlines();

    frecOcupadas = []

    for l in mybytes:
        mystr = l.decode("utf8")
        if mystr.find("MHz") > 0:
            mystr = mystr.replace("<td>", "")
            mystr = mystr.replace("</td>", "")
            mystr = mystr.replace("MHz", "")
            frecOcupadas.append(float(mystr))

    fp.close()
    return sort(frecOcupadas)

allFrec = []
for i in arange(87.5,108,0.1):
    allFrec.append(round(i, 1));

localidad = getFrecOcupadas("https://frecuenciasradio.com/localidad/benalmadena")
# localidad2 = getFrecOcupadas("https://frecuenciasradio.com/localidad/chipiona")

# print(Diff(localidad, localidad2))

# l = []

# for e in localidad:
#     l.append(e)
# for e in localidad2:
#     l.append(e)

# localidad = sort(l)

localidadLibre = Diff(localidad, allFrec)

# print (localidad)
# print (localidadLibre)

# malaga = getFrecLibres("https://frecuenciasradio.com/localidad/malaga")
# torremolinos = getFrecLibres("https://frecuenciasradio.com/localidad/torremolinos")


distInfMax = 0
distSupMax = 0
frecOp = 0
for f in localidadLibre:
    distInf = 0
    distSup = 0
    i = 0
    while i < len(localidad) and f - localidad[i] > 0:
        distInf = f - localidad[i]
        i += 1
        
    if i >= len(localidad):
        distSup = 10
    else: 
        distSup = localidad[i] - f

    if(distInfMax < distInf and distSupMax < distSup):
        distInfMax = distInf
        distSupMax = distSup
        frecOp = f

print()
print("Optimo para: ")
print(frecOp)
print()

