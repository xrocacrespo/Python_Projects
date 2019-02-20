import maya.cmds as mc
from functools import partial
def returnType(s=False, type='mesh'):
    '''
    Funcio que retorna les llums d'un grup d'objectes seleccionars
    :return lights[]:
    :param s:
    '''
    lights=[]
    sel = mc.ls(sl=True, type='transform')
    for obj in sel:
        shapes = mc.listRelatives(obj, children=True)
        if shapes != None:
            tipus = mc.objectType(shapes[0]).lower()
            if tipus.endswith(type):
                if s == True:
                    lights.append(shapes[0])
                else:
                    lights.append(obj)
    return lights

# llums = returnType(s=True, type='light')
# for i in llums:
#     mc.setAttr(i + '.intensity', 20)
#
# joints = returnType(s=True, type='mesh')
# print joints

###############
#   CLOSURE   #
###############

def makeCube(x):
    cube = mc.polyCube(n='cube' + str(x+1))
    return cube
def cubeStack(numCubes = 10):
    '''
    Apila cubs
    :param numCubes: 
    :return: 
    '''

    for i in range(numCubes):
        cube = makeCube(i)
        mc.setAttr(cube[0]+'.ty', i+0.5)

# cubeStack(30)

def cubeStack2(numCubes = 10):
    '''
    Apila cubs
    :param numCubes:
    :return:
    '''

    def makeCube2():
        cube = mc.polyCube(n='cube' + str(i + 1))
        return cube

    for i in range(numCubes):
        cube = makeCube2()
        mc.setAttr(cube[0]+'.ty', i+0.5)

# cubeStack2()

###############
#   SCOPE     #
###############
'''
Les variables son accessibles depen d'on estiguin declarades.
varA es accessible per tots.
varB es accessible dintre de FuncioX
varC es accessible dintre de enclosedFunc
'''

varA = 10
def FuncioX(varX):
    varB = varX * 2.0
    print ('varB: ' + str(varB))
    def enclosedFunc():
        varC = varB + varA
        print ('varC: ' + str(varC))
    enclosedFunc()
# FuncioX(2)

###########################
#   String formatting     #
###########################

    # VERSIO ANTIGA

import os
print('Aquest usuari es: %s' %os.getenv("USERNAME"))
print('Aquest usuari es: ' + os.getenv("USERNAME"))

print ('un string qualsevol %s %s %s' % (1,2,3))
# 'un string qualsevol 1 2 3'
nom = 'Xavi'
cognom = 'Roca'
print ('El nom real del Pingui es : %s %s' % (nom, cognom))
# 'El nom real del Pingui es : Xavi Roca'

identity = {'nom':'Xavi', 'cognom':'Roca'}
print ('El nom real del Pingui es : %(nom)s %(cognom)s' % identity)
# 'El nom real del Pingui es : Xavi Roca'


import random
# print random.random()
unFloat = random.random() * 100
print('com un int: %i' %unFloat)
print('com un int: %f' %unFloat)

print('com un int: %d' %unFloat)
# un digit

print('com un int: %0.2f' %unFloat)
# 0.00
print('com un int: %010.2f' %unFloat)
# 00000000.00
print('com un int: %010.2e' %unFloat)
# 000.00e+00
print('com un int: %-010.2e' %unFloat)
# 0.00e+00 (es carrega tots els 0 que hi ha a l'esquerre

    # VERSIO NOVA

print 'Un string qualsevol {}'.format(100)

print 'Un string qualsevol {0} i un altre {1}'.format('Hola', 'Adeu')

identity = {'nom':'Xavi', 'cognom':'Roca', 'cognom2':'Crespo'}
identity2 = ['Xavi','Roca']
identity3 = [['Xavi','Roca'],['Javier','Crespo']]
# print 'El nom real del PINGUI es: {0} {1}'.format(identity['nom'],identity['cognom'])
#
# print 'El nom real del PINGUI es: {nom} {cognom}'.format(**identity)
#
# print 'El nom real del PINGUI es: {0} {1}'.format(*identity2)

print 'El nom real del PINGUI es: {0} {1}'.format(*[a for a in b in identity3])

test = 3.8415
print('Com un enter: %d' %test)
# Com un enter: 3
print('Com un enter: {0:.0f}'.format(test))
# Com un enter: 4
print('Com un float: {0:.8f}'.format(test))
# Com un float: 3.84150000
print('Com un enter: {0}'.format(int(test)))
# Com un enter: 3.000000








