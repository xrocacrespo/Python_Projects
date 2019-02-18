import maya.cmds as mc

myCube = mc.polyCube()
 # Aixo retorna [u'pCube1', u'polyCube1'], dos objectes.

mc.polyCube(myCube[1], q=True, sy=True)
# Query de les subdivision en height del cub (li passem el historial en aquest cas)



