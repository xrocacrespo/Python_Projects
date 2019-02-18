'''
Crear una escala de cargol amb 20 graons
Comentar el codi
Utilitzar el range() command en un for loop per generar nombres enters
Punts extres si utilitzem diccionari.
'''
# imports
import maya.cmds as mc

# Creacio del File de 0
def newFile():
    mc.file('pythonModel', force=True, new=True)
    
# Posem MATERIALS!
def createMats(node, matType, rr, rb, rg):
    if mc.objExists(node):
        shd = mc.shadingNode(matType, name="{}_{}".format(node,matType), asShader=True)
        mc.setAttr('{}.color'.format(shd), rr, rb, rg)
        shdSG = mc.sets(name='{}SG'.format(shd), empty=True, renderable=True, noSurfaceShader=True)
        mc.connectAttr('{}.outColor'.format(shd), '{}.surfaceShader'.format(shdSG))
        mc.sets(node, e=True, forceElement=shdSG)

# Definim el diciconari de valors

settings = {
	'nameStep':'step',
	'numSteps':100,
	'widthStep' : 5,
	'heightStep': 0.2,
	'depthStep': 2,
	'offsetStep': 0.5,

	'radius': 2,
	'degrees': 10,

	'heightHandBar':4,
	'radiusHandBar':0.2,
	'createHandBar':True,
	'radiusUpBars': 0.1,
	'radiusHandleSpheres': 1,

	'createCenterCol':True
	}


	
def construccioGrao(numStep,nameStep):

	'''

	DOCSTRING: aixo es l'ajuda de la funcio

	:param numStep:
	:param nameStep:
	:return:
	'''

	step = mc.polyCube(name='{}_{}_geo'.format(nameStep, numStep), w=settings['widthStep'], h=settings['heightStep'], d=settings['depthStep'])
	reversedHalfWidth = settings['widthStep'] * -1 * 0.5
	halfHeight = settings['heightStep'] * 0.5
	mc.move(reversedHalfWidth, halfHeight, 0,step[0])

	step_grp = mc.group(n='{}_{}_grp'.format(nameStep, numStep), em=True)
	mc.parent(step[0], step_grp)

	upbar_handBar = mc.polyCylinder(n='upBar{}_geo'.format(numStep), h=settings['heightHandBar'],
									r=settings['radiusUpBars'])
	mc.move(-settings['widthStep'] + settings['radiusUpBars'], settings['heightHandBar'] / 2.0, 0, upbar_handBar[0])
	mc.parent(upbar_handBar[0], step_grp)

	locator_railing = mc.spaceLocator(n='handBar_{}_LOC'.format(numStep),
									  position=[-settings['widthStep'] + settings['radiusUpBars'],
												settings['heightHandBar'], 0])
	mc.setAttr(locator_railing[0] + '.visibility', False)
	mc.parent(locator_railing[0], step_grp)

	mc.move(settings['radius'] * -1, 0, 0, step_grp)

	radius_grp = mc.group(n='{}_{}_radOff_grp'.format(nameStep, numStep), em=True)
	mc.parent(step_grp, radius_grp)



	mc.rotate(0,numStep*settings['degrees'],0,radius_grp)
	mc.move(0,numStep*(settings['heightStep']+settings['offsetStep']),0, radius_grp)

	mc.parent(radius_grp, steps_grp)


		
def createHandBar():
	handBar_grp = mc.group(em=True, n='handbar_grp')
	mc.parent(handBar_grp, master_grp)
	mc.select('handBar*LOC')
	list_locators = mc.ls(selection=True)
	list_pos = []
	for i, loc in enumerate(list_locators):
		p = mc.pointPosition(loc, world=True)
		list_pos.append(p)
		if i == 0:
			initial_sphere, initial_sphereHist = mc.polySphere(n='initialSphere_geo',r=settings['radiusHandleSpheres'])
			mc.move(p[0],p[1],p[2], initial_sphere)
		if i == len(list_locators)-1:
			last_sphere, last_sphereHist = mc.polySphere(n='lastSphere_geo', r=settings['radiusHandleSpheres'])
			mc.move(p[0], p[1], p[2], last_sphere)

	curve_railing = mc.curve(n='curveRailing',p=list_pos)
	shape_railing = mc.circle(n='shapeRailing',r=settings['radiusHandBar'])

	handBar = mc.extrude(shape_railing[0], curve_railing, useComponentPivot=1, fixedPath=True, useProfileNormal=True, name='railing_geo')
	mc.delete(list_locators, curve_railing, shape_railing)
	mc.parent(handBar[0], handBar_grp)

def createCenterCol():
	print 'Columna Central'
	centerCol = mc.polyCylinder(n='centerColumn_geo', r= settings['radius'], h= (settings['numSteps'] * (settings['heightStep'] + settings['offsetStep']))+settings['heightHandBar'])
	mc.xform(centerCol[0], t=[0,(mc.getAttr(centerCol[1] + '.h'))/2.0, 0])

# BUILD
newFile()
master_grp = mc.group(em=True, n='stairs_grp')

steps_grp = mc.group(em=True, n='steps_grp')
mc.parent(steps_grp, master_grp)


help(construccioGrao)
for i in range(settings['numSteps']):
	construccioGrao(i,settings['nameStep'])
if settings['createHandBar']:
	createHandBar()
if settings['createCenterCol']:
	createCenterCol()
mc.viewFit(all=True)