# imports
import maya.cmds as mc
import random as rnd

# Creacio del File de 0
def newFile(filename='pythonModel'):
    """
    creeacio de arxiu nou
    :return:
    """
    mc.file(filename, force=True, new=True)

def createMats(nameMat, matType='phong', color=[1.0, 1.0, 1.0], *args, **kwargs):
    """"
    Modul de creacio de materials

    :param nameMat: nom del material
    :param matType: tipus de material
    :param color: array de floats
    :param args:
    :param kwargs:
    :return shd: shading group
    """

    shd = mc.shadingNode(matType, name="{}_{}_SHD".format(nameMat,matType), asShader=True)
    mc.setAttr('{}.color'.format(shd), color[0], color[1], color[2])
    shdSG = mc.sets(name='{}SG'.format(shd), empty=True, renderable=True, noSurfaceShader=True)
    mc.connectAttr('{}.outColor'.format(shd), '{}.surfaceShader'.format(shdSG))

    return shd

def xavierRocaCrespo_ex1(groupName='botBunny',smoothGeo=False, *args, **kwargs):
    """
    Crea un ninot tipus Conill Robotic

    :param groupName: nom del modul
    :param smoothGeo: si es vol fer el smooth de la mesh o nomes fer-lo visible
    :param args:
    :param kwargs:
    :return global_grp: retorna el grup del modul sencer
    """
    counter = 0

    # MASTER GROUP
    moduleName = '{0}_{1}'.format(groupName, str(counter))
    while mc.objExists('{}_GRP'.format(moduleName)):
        counter = counter + 1
        moduleName = '{0}_{1}'.format(groupName, counter)

    global_grp = mc.group(n=moduleName+'_GRP', em=True)

    # MATERIAL LIST
    material_list={}

    # Creacio materials
    def creacioMaterials(materialType='lambert', *args, **kwargs):
        """
        Omple la llista de materials

        :param materialType: tipus de material per tot el model
        :param args:
        :param kwargs:
        :return:
        """
        material_list['red'] = createMats('{}_red'.format(moduleName), matType=materialType, color=[0.250, 0, 0])
        material_list['black'] = createMats('{}_black'.format(moduleName), matType=materialType, color=[0.05, 0.05, 0.05])
        material_list['white'] = createMats('{}white'.format(moduleName), matType=materialType, color=[1, 1, 1])

    # Creacio de les orelles
    def creacioOrelles(*args, **kwargs):
        """
        Creacio de les orelles

        :param args:
        :param kwargs:
        :return:
        """
        ears=[]
        for side in ['L','R']:
            subModuleName = '{0}_ear{1}'.format(side, moduleName)
            name_geo = '{0}_geo'.format(subModuleName)
            ear = mc.polyCube(name=name_geo,sw=4, sh=2, sd=2)
            mc.setAttr(ear[1] + '.height',5)
            mc.setAttr(ear[1] + '.width', 2)
            mc.select(ear[0] + '.e[43:45]')
            mc.select(ear[0] + '.e[48:50]', add=True)
            mc.move(0,2,0, r=True)
            mc.select(ear[0] + '.e[45]')
            mc.select(ear[0] + '.e[50]', add=True)
            mc.select(ear[0] + '.e[43]', add=True)
            mc.select(ear[0] + '.e[48]', add=True)
            mc.move(0,-0.2,0, r=True)
            mc.select(ear[0] + '.f[6]')
            mc.select(ear[0] + '.f[7]', add=True)
            mc.select(ear[0] + '.f[3]', add=True)
            mc.select(ear[0] + '.f[2]', add=True)
            mc.polyExtrudeFacet(thickness=-0.1, scale= [0.7,0.7,0.7])
            mc.select(ear[0] + '.f[24:31]')
            mc.polyExtrudeFacet(scale=[0.7, 0.7, 0.7])
            ear_connection = mc.polyCube(name='{0}_earConnection{1}_geo'.format(side,moduleName), w=0.7, h=2, d=0.7, sw=5, sh=5, sd=5)
            mc.move(0, -3.5, 0, ear_connection)

            # Shading
            mc.select(ear[0])
            mc.hyperShade(a=material_list['red'])

            mc.select(ear_connection[0])
            mc.hyperShade(a=material_list['black'])

            # Grouping
            mc.select(ear[0], ear_connection[0])
            ear_grp = mc.group(name='{0}_grp'.format(subModuleName))
            ears.append(ear_grp)

            # To global
            mc.parent(ear_grp, global_grp)

        l_ear= ears[0]
        r_ear= ears[1]

        # POSITION AND SCALE
        mc.scale(-1.345, 1.345, 1.345, r_ear)
        mc.move(4.232, 26.36, -3.592, r_ear)
        mc.rotate(-21.168, 7.997, -29.047, r_ear)
        mc.scale(1.345, 1.345, 1.345, l_ear)
        mc.move(-4.232, 26.36, -3.592, l_ear)
        mc.rotate(-21.168, -7.997, 29.047, l_ear)

    # Creacio del cap
    def creacioCap(*args, **kwargs):
        """
        Creacio del cap

        :param args:
        :param kwargs:
        :return:
        """
        subModuleName = 'C_head{0}'.format(moduleName)
        name_geo = '{}_geo'.format(subModuleName)
        head = mc.polySphere(name=name_geo, r=5, sa=10, sh=10)
        mc.scale(0.9,0.9,1)
        mc.rotate(90,0,0)
        mc.select(head[0] + '.f[90:99]')
        mc.polyExtrudeFacet(thickness=0, scale=[0.7, 0.7, 0.7])
        mc.polyExtrudeFacet(thickness=-0.5)
        mc.select(head[0] + '.f[100:109]')
        mc.polyExtrudeFacet(thickness=0.3)
        mc.select(head[0] + '.e[80:89]')
        bevel_deform1 = mc.polyBevel()
        mc.setAttr(bevel_deform1[0] + '.offsetAsFraction', 1)
        mc.setAttr(bevel_deform1[0] + '.mergeVertices', 1)
        mc.setAttr(bevel_deform1[0] + '.fraction', 0.3)
        mc.setAttr(bevel_deform1[0] + '.smoothingAngle', 30)
        mc.setAttr(bevel_deform1[0] + '.segments', 2)

        mc.select(head[0]+'.e[200]',
                  head[0] + '.e[206]',
                  head[0] + '.e[210]',
                  head[0] + '.e[214]',
                  head[0] + '.e[218]',
                  head[0] + '.e[222]',
                  head[0] + '.e[226]',
                  head[0] + '.e[230]',
                  head[0] + '.e[234]',
                  head[0] + '.e[238]')
        bevel_deform2 = mc.polyBevel()
        mc.setAttr(bevel_deform2[0] + '.offsetAsFraction', 1)
        mc.setAttr(bevel_deform2[0] + '.mergeVertices', 1)
        mc.setAttr(bevel_deform2[0] + '.fraction', 0.3)
        mc.setAttr(bevel_deform2[0] + '.smoothingAngle', 30)
        mc.setAttr(bevel_deform2[0] + '.segments', 2)

        mc.select(head[0] + '.e[202]',
                  head[0] + '.e[204]',
                  head[0] + '.e[206]',
                  head[0] + '.e[208]',
                  head[0] + '.e[210]',
                  head[0] + '.e[212]',
                  head[0] + '.e[214]',
                  head[0] + '.e[216]',
                  head[0] + '.e[218]',
                  head[0] + '.e[219]')
        bevel_deform3 = mc.polyBevel()
        mc.setAttr(bevel_deform3[0] + '.offsetAsFraction', 1)
        mc.setAttr(bevel_deform3[0] + '.mergeVertices', 1)
        mc.setAttr(bevel_deform3[0] + '.fraction', 0.3)
        mc.setAttr(bevel_deform3[0] + '.smoothingAngle', 30)
        mc.setAttr(bevel_deform3[0] + '.segments', 2)
        mc.move(0, 18.606, 0, head[0])

        # Creacio Eyes
        eyes = mc.polyCube(n='C_eyes{}_geo'.format(moduleName), sw=2, sh=2, sd=2)
        mc.xform(eyes[0], t=[0,21.234,3.785], ro=[-11.618,0,0], s=[6.136,2.055,1.653])
        mc.select('{}.f[0:3]'.format(eyes[0]))
        mc.polyExtrudeFacet(thickness=0, scale=[0.9, 0.9, 0.9])
        mc.polyExtrudeFacet(thickness=0, scale=[0.9, 0.9, 0.9])
        mc.polyExtrudeFacet(thickness=-0.2)
        mc.polyExtrudeFacet(thickness=-0.2)

        # Shading
        mc.select(head[0])
        mc.hyperShade(a=material_list['white'])

        mc.select(eyes[0])
        mc.hyperShade(a=material_list['black'])

        mc.select('{}.f[48:55]'.format(eyes[0]), '{}.f[0:3]'.format(eyes[0]))
        mc.hyperShade(a=material_list['red'])

        # Grouping
        head_grp = mc.group(n='{}_grp'.format(subModuleName), em=True)
        mc.parent(head[0], eyes[0], head_grp)

        # To global
        mc.parent(head_grp, global_grp)

    # Creacio del body
    def creacioBody(*args, **kwargs):
        """
        Creacio del cos

        :param args:
        :param kwargs:
        :return:
        """
        subModuleName = 'C_body{0}'.format(moduleName)
        name_geo = '{0}_geo'.format(subModuleName)
        body = mc.polyCube(name=name_geo, w=2, h=4, d=2, sh=2, sd=2, sw=3)
        mc.select(body[0]+'.e[9:11]')
        mc.move(0,0,-0.5, r=True)
        mc.select(body[0] + '.e[6:8]')
        mc.move(0, 0, -1, r=True)
        mc.select(body[0] + '.f[18:23]')
        mc.scale(0.5,1,1)
        mc.select(body[0] + '.vtx[20:23]')
        mc.move(0,0,0.3, r=True)
        mc.select(body[0] + '.e[21:23]')
        mc.move(0, -1, 0, r=True)

        # POSITION AND SCALE
        mc.scale(2.4, 2.4, 2.4, body[0])
        mc.move(0, 8.465, 1.524, body[0])

        # Shading
        mc.select(body[0])
        mc.hyperShade(a=material_list['white'])

        # COLL
        coll = mc.polyCube(name='C_neck{}_geo'.format(moduleName), sw=2, sh=2, sd=2)
        mc.move(0,13.623,0, coll[0])


        # Grouping
        body_grp = mc.group(n='{0}_grp'.format(subModuleName), em=True)
        mc.parent(body[0], coll[0], body_grp)

        # To global
        mc.parent(body_grp, global_grp)

    # Creacio dels Arms
    def creacioArms(*args, **kwargs):
        """
        Creacio dels arms

        :param args:
        :param kwargs:
        :return:
        """
        arms = []
        for side in ['L','R']:
            subModuleName1 = '{0}_arm01{1}_geo'.format(side, moduleName)
            arm_part1 = mc.polyCube(n=subModuleName1, w=2, h=4, d=2, sh=2, sd=2, sw=3)
            mc.select(arm_part1[0] + '.f[1]',arm_part1[0] + '.f[22]')
            mc.scale(1.5,1,1, r=True)
            mc.polyExtrudeFacet(thickness=-0.4)
            mc.polyExtrudeFacet(thickness=-0.4)
            mc.move(0, 2, 0, arm_part1[0])

            subModuleName2 = '{0}_arm02{1}_geo'.format(side, moduleName)
            arm_part2 = mc.polySphere(n=subModuleName2, sa=6, sh=6)
            mc.move(0,0,0.889, arm_part2[0])
            mc.scale(1, 2.522, 1, arm_part2[0])

            subModuleName3 = '{0}_arm03{1}_geo'.format(side, moduleName)
            arm_part3 = mc.duplicate(arm_part1[0], n=subModuleName3)
            mc.move(-0.027, -2.777, 0.67, arm_part3)
            mc.rotate(-33.848, 0, 0, arm_part3)
            mc.scale(1, -1, 1, arm_part3)

            #HAND
            subModuleName4 = '{0}_hand01{1}_geo'.format(side, moduleName)
            arm_part4 = mc.polyCube(n=subModuleName4, sw=3, sh=3, sd=3)
            mc.move(-0.279, -5.082, 2.266, arm_part4[0])
            mc.rotate(-34.836, 0, 0, arm_part4[0])
            mc.scale(0.775, 1.354, 1.445, arm_part4[0])
            mc.move(0,0.148768,0, arm_part4[0]+'.f[12:14]', r=True )

            subModuleName5 = '{0}_hand02{1}_geo'.format(side, moduleName)
            arm_part5 = mc.polyCube(n=subModuleName5, sw=3, sh=3, sd=3)
            mc.move(0.49, -4.837, 2.105, arm_part5[0])
            mc.rotate(-37.317, 0, 0, arm_part5[0])
            mc.scale(0.473, 1, 1, arm_part5[0])

            arm_group = mc.group(
                arm_part1[0],
                arm_part2[0],
                arm_part3[0],
                arm_part4[0],
                arm_part5[0],
                n='{}_arm{}_grp'.format(side,moduleName))
            arms.append(arm_group)

            # JUNTES
            subModuleName6 = '{0}_junta01{1}_geo'.format(side, moduleName)
            arm_part6 = mc.polyCylinder(n=subModuleName6, sa=12, sh=3, sc=2)
            mc.xform(arm_part6[0], s=[0.389, 1.565, 0.389], t=[0.286, 3.178, 0.044], ro=[0, 0, -90])
            mc.parent(arm_part6[0], arm_group)

            # To global
            mc.parent(arm_group, global_grp)

            # Shading
            mc.select(arm_part1[0], arm_part3[0])
            mc.hyperShade(a=material_list['white'])

            mc.select(arm_part2[0], arm_part4[0],  arm_part5[0], arm_part6[0])
            mc.hyperShade(a=material_list['black'])

        l_arm = arms[0]
        r_arm = arms[1]

        # POSITION AND SCALE
        mc.move(-4.545, 9.592, 0.873, l_arm)
        mc.rotate(0, 0, -18, l_arm)
        mc.scale(0.834, 0.834, 0.834, l_arm)

        mc.move(4.545, 9.592, 0.873, r_arm)
        mc.rotate(0, 0, 18, r_arm)
        mc.scale(-0.834, 0.834, 0.834, r_arm)

    # Creacio dels Legs
    def creacioLegs(*args, **kwargs):
        """
        Creacio de les cames

        :param args:
        :param kwargs:
        :return:
        """
        legs = []
        for side in ['L', 'R']:
            subModuleName1 = '{0}_leg01{1}_geo'.format(side, moduleName)
            leg_part1 = mc.polyCube(n=subModuleName1, w=3.5, h=3.5, d=3.5, sh=2, sw=3)
            mc.scale(0.526, 1.939, 0.961, leg_part1[0])
            mc.move(-2.07, 3.346, 1.48, leg_part1[0])
            mc.select(leg_part1[0]+'.vtx[4:7]', leg_part1[0]+'.vtx[16:19]')
            mc.move(0, 0.4, 0.8, r=True)
            mc.scale(1, 1.5, 1.5)
            mc.select(leg_part1[0] + '.vtx[16:19]')
            mc.move(0, 0, 1.7, r=True)
            mc.select(leg_part1[0] + '.vtx[0:3]', leg_part1[0] + '.vtx[20:23]')
            mc.scale(0.5, 1, 0.6)

            subModuleName2 = '{0}_leg02{1}_geo'.format(side, moduleName)
            leg_part2 = mc.polyCube(n=subModuleName2, sw=2, sh=2, sd=3)
            mc.move(-2.029, -0.494, 2.95, leg_part2[0])
            mc.scale(2.078, 0.751, 8.619, leg_part2[0])
            mc.rotate(17.419, 0, 0, leg_part2[0])
            mc.select(leg_part2[0]+'.f[4:5]', leg_part2[0]+'.f[22]', leg_part2[0]+'.f[25]', leg_part2[0]+'.f[28]', leg_part2[0]+'.f[31]', leg_part2[0]+'.f[0:3]')
            mc.polyExtrudeFacet(thickness=0.1)
            mc.polyExtrudeFacet(thickness=0.1)
            mc.select(leg_part2[0] + '.f[4:5]', leg_part2[0] + '.f[22]', leg_part2[0] + '.f[25]', leg_part2[0] + '.f[28]',
                      leg_part2[0] + '.f[31]')
            mc.polyConnectComponents()
            mc.select(leg_part2[0] + '.e[107]', leg_part2[0] + '.e[85]')
            mc.move(0,0.492567,0, r=True)

            # JUNTES
            subModuleName3 = '{0}_junta02{1}_geo'.format(side, moduleName)
            leg_part3 = mc.polyCylinder(n=subModuleName3, sa=12, sh=3, sc=2)
            mc.xform(leg_part3[0], s=[0.736, 1.565, 0.736], t=[-1.632, 5.52, 1.879], ro=[0, 0, -90])

            # Shading
            mc.select(leg_part1[0], leg_part2[0])
            mc.hyperShade(a=material_list['white'])

            mc.select(leg_part3[0])
            mc.hyperShade(a=material_list['black'])

            mc.select('{}.f[6:19]'.format(leg_part2[0]), '{}.f[20:21]'.format(leg_part2[0]), '{}.f[23:24]'.format(leg_part2[0]), '{}.f[26:27]'.format(leg_part2[0]), '{}.f[29:30]'.format(leg_part2[0]), '{}.f[34:35]'.format(leg_part2[0]), '{}.f[37:38]'.format(leg_part2[0]), '{}.f[40:41]'.format(leg_part2[0]))
            mc.hyperShade(a=material_list['red'])

            leg_grp = mc.group(em=True, n='{0}_leg{1}_grp'.format(side,moduleName))
            mc.parent(leg_part1[0], leg_part2[0], leg_part3[0], leg_grp)
            legs.append(leg_grp)

            # To global
            mc.parent(leg_grp, global_grp)

            if side == 'R':
                mc.scale(-1, 1, 1, leg_grp)
                mc.move(1, 0, 0, leg_grp)
            else:
                mc.move(-1, 0, 0, leg_grp)

    # Creacio del la Cua
    def creacioCua(*args, **kwargs):
        """
        Creacio de la cua

        :param args:
        :param kwargs:
        :return:
        """
        subModuleName = 'C_tail{0}_geo'.format(moduleName)
        cua = mc.polySphere(n=subModuleName, sa=10, sh=10, r=2)
        mc.move(0,4.197,-2.285, cua[0])

        # To global
        mc.parent(cua[0], global_grp)

        # Shading
        mc.select(cua[0])
        mc.hyperShade(a=material_list['white'])

    # SMOOTH ALL
    def smoothAll(*args, **kwargs):
        """
        Smooth a la geometria

        :param args:
        :param kwargs:
        :return:
        """
        # SMOOTH FOR ALL GEO
        all_geo = mc.listRelatives(global_grp, ad=True)
        if smoothGeo:
            for obj in all_geo:
                mc.polySmooth(obj)
                mc.select(cl=True)
        else:
            mc.select(global_grp)
            mc.displaySmoothness(po=3)
            mc.select(cl=True)

    # BUILD
    creacioMaterials(materialType='phong')
    creacioOrelles()
    creacioCap()
    creacioBody()
    creacioArms()
    creacioLegs()
    creacioCua()
    smoothAll()

    # REPOSITION
    mc.xform(global_grp, translation=[0, 3, 0], rotation=[10, 0, 0], zeroTransformPivots=True)
    temp_group = mc.listRelatives(global_grp, c=True)
    mc.parent(temp_group, w=True)
    mc.xform(global_grp, translation=[0, 0, 0], rotation=[0, 0, 0], zeroTransformPivots=True)
    mc.parent(temp_group, global_grp)
    mc.select(cl=True)

    return global_grp

def xavierRocaCrespo_ex2(groupName='stairs',
                         nameStep='step',
                         numSteps=100,
                         widthStep=5,
                         heightStep=0.2,
                         depthStep=2,
                         offsetStep=0.5,
                         radius=2,
                         degrees=10,
                         heightHandBar=4,
                         radiusHandBar=0.2,
                         createHandBar=True,
                         radiusUpBars=0.1,
                         radiusHandleSpheres=1,
                         createCenterCol=True,
                         *args,
                         **kwargs):
    """
        Crea unes escales de cargol

        :param groupName: nom del modul
        :param args:
        :param kwargs:
        :return global_grp: retorna el grup del modul sencer
    """

    #############
    # SEETTINGS #
    #############
    settings = {
        'nameStep': nameStep,
        'numSteps': numSteps,
        'widthStep': widthStep,
        'heightStep': heightStep,
        'depthStep': depthStep,
        'offsetStep': offsetStep,
        'radius': radius,
        'degrees': degrees,
        'heightHandBar': heightHandBar,
        'radiusHandBar': radiusHandBar,
        'createHandBar': createHandBar,
        'radiusUpBars': radiusUpBars,
        'radiusHandleSpheres': radiusHandleSpheres,
        'createCenterCol': createCenterCol
    }

    counter = 0

    ################
    # MASTER GROUP #
    ################
    moduleName = '{0}_{1}'.format(groupName, str(counter))
    while mc.objExists('{}_GRP'.format(moduleName)):
        counter = counter + 1
        moduleName = '{0}_{1}'.format(groupName, counter)
    global_grp = mc.group(n=moduleName + '_GRP', em=True)



    #################
    # MATERIAL LIST #
    #################
    material_list = {}

    def creacioMaterials(materialType='lambert', *args, **kwargs):
        """
        Omple la llista de materials

        :param materialType: tipus de material per tot el model
        :param args:
        :param kwargs:
        :return:
        """
        material_list['red'] = createMats('{}_red'.format(moduleName), matType=materialType, color=[0.250, 0, 0])
        material_list['black'] = createMats('{}_black'.format(moduleName), matType=materialType, color=[0.1, 0.1, 0.1])
        material_list['white'] = createMats('{}white'.format(moduleName), matType=materialType, color=[1, 1, 1])
        material_list['gold'] = createMats('{}gold'.format(moduleName), matType=materialType, color=[1, 0.7, 0])
        material_list['grey'] = createMats('{}grey'.format(moduleName), matType=materialType, color=[0.3, 0.3, 0.3])

    def construccioGrao(numStep, nameStep, *args, **kwargs):
        '''
        Construeix un grao

        :param numStep:
        :param nameStep:
        :return:
        '''

        step = mc.polyCube(name='{0}{1}_{2}_geo'.format(moduleName, nameStep, numStep), w=settings['widthStep'],
                           h=settings['heightStep'], d=settings['depthStep'])
        # Shading
        if numStep % 2:
            mc.select(step[0])
            mc.hyperShade(a=material_list['black'])
        else:
            mc.select(step[0])
            mc.hyperShade(a=material_list['white'])


        reversedHalfWidth = settings['widthStep'] * -1 * 0.5
        halfHeight = settings['heightStep'] * 0.5
        mc.move(reversedHalfWidth, halfHeight, 0, step[0])

        step_grp = mc.group(n='{0}{1}_{2}_grp'.format(moduleName, nameStep, numStep), em=True)
        mc.parent(step[0], step_grp)

        upbar_handBar = mc.polyCylinder(n='{0}upBar{1}_geo'.format(moduleName, numStep), h=settings['heightHandBar'],
                                        r=settings['radiusUpBars'])
        # Shading
        mc.select(upbar_handBar[0])
        mc.hyperShade(a=material_list['grey'])

        mc.move(-settings['widthStep'] + settings['radiusUpBars'], settings['heightHandBar'] / 2.0, 0, upbar_handBar[0])
        mc.parent(upbar_handBar[0], step_grp)

        locator_railing = mc.spaceLocator(n='{0}handBar_{1}_LOC'.format(moduleName, numStep),
                                          position=[-settings['widthStep'] + settings['radiusUpBars'],
                                                    settings['heightHandBar'], 0])
        mc.setAttr(locator_railing[0] + '.visibility', False)
        mc.parent(locator_railing[0], step_grp)

        mc.move(settings['radius'] * -1, 0, 0, step_grp)

        radius_grp = mc.group(n='{0}{1}_{2}_radOff_grp'.format(moduleName, nameStep, numStep), em=True)
        mc.parent(step_grp, radius_grp)

        mc.rotate(0, numStep * settings['degrees'], 0, radius_grp)
        mc.move(0, numStep * (settings['heightStep'] + settings['offsetStep']), 0, radius_grp)

        mc.parent(radius_grp, steps_grp)

    def createHandBar(*args, **kwargs):
        """
        Crea la barra de pasamans

        :param args:
        :param kwargs:
        :return:
        """
        handBar_grp = mc.group(em=True, n='{}handbar_grp'.format(moduleName))
        mc.parent(handBar_grp, global_grp)
        mc.select('*handBar*LOC')
        list_locators = mc.ls(selection=True)
        list_pos = []
        for i, loc in enumerate(list_locators):
            p = mc.pointPosition(loc, world=True)
            list_pos.append(p)
            if i == 0:
                initial_sphere, initial_sphereHist = mc.polySphere(n='{}initialSphere_geo'.format(moduleName),
                                                                   r=settings['radiusHandleSpheres'])
                # Shading
                mc.select(initial_sphere)
                mc.hyperShade(a=material_list['gold'])

                mc.move(p[0], p[1], p[2], initial_sphere)
                mc.parent(initial_sphere, global_grp)
            if i == len(list_locators) - 1:
                last_sphere, last_sphereHist = mc.polySphere(n='{}lastSphere_geo'.format(moduleName), r=settings['radiusHandleSpheres'])

                # Shading
                mc.select(last_sphere)
                mc.hyperShade(a=material_list['gold'])

                mc.move(p[0], p[1], p[2], last_sphere)
                mc.parent(last_sphere, global_grp)

        curve_railing = mc.curve(n='{}curveRailing'.format(moduleName), p=list_pos)
        shape_railing = mc.circle(n='{}shapeRailing'.format(moduleName), r=settings['radiusHandBar'])

        handBar = mc.extrude(shape_railing[0], curve_railing, useComponentPivot=1, fixedPath=True,
                             useProfileNormal=True, name='{}railing_geo'.format(moduleName))

        # Shading
        mc.select(handBar[0])
        mc.hyperShade(a=material_list['gold'])

        mc.delete(list_locators, curve_railing, shape_railing)
        mc.parent(handBar[0], handBar_grp)

    def createCenterCol(*args, **kwargs):
        """
        Crea una columna Central

        :param args:
        :param kwargs:
        :return:
        """
        centerCol, centerColHist = mc.polyCylinder(n='{}centerColumn_geo'.format(moduleName), r=settings['radius'],
                                    h=(settings['numSteps'] * (settings['heightStep'] + settings['offsetStep'])) +
                                      settings['heightHandBar'])
        # Shading
        mc.select(centerCol)
        mc.hyperShade(a=material_list['black'])

        mc.parent(centerCol,global_grp)
        mc.xform(centerCol, t=[0, (mc.getAttr(centerColHist + '.h')) / 2.0, 0])

    #########
    # BUILD #
    #########

    steps_grp = mc.group(em=True, n='{}steps_grp'.format(moduleName))
    mc.parent(steps_grp, global_grp)

    creacioMaterials()

    for i in range(settings['numSteps']):
        construccioGrao(i, settings['nameStep'])
    if settings['createHandBar']:
        createHandBar()
    if settings['createCenterCol']:
        createCenterCol()

    mc.select(cl=True)
    return global_grp

newFile(filename='xavierRocaCrespo_ex3')

exec1 = xavierRocaCrespo_ex1('botBunny', smoothGeo=False)
exec2 = xavierRocaCrespo_ex1('botBunny', smoothGeo=False)

exec3 = xavierRocaCrespo_ex2()
exec4 = xavierRocaCrespo_ex2('stairs2',
                         nameStep='step',
                         numSteps=200,
                         widthStep=5,
                         heightStep=0.2,
                         depthStep=2,
                         offsetStep=0.5,
                         radius=5,
                         degrees=10,
                         heightHandBar=4,
                         radiusHandBar=0.2,
                         createHandBar=True,
                         radiusUpBars=0.1,
                         radiusHandleSpheres=1,
                         createCenterCol=False)

mc.xform(exec1, t=[rnd.randrange(-100.0, 50.0, 10.0), 0, rnd.randrange(-100.0, 50.0, 10.0)], ro=[0, rnd.randrange(0.0, 360.0, 10.0), 0])
mc.xform(exec2, t=[rnd.randrange(-100.0, 50.0, 10.0), 0, rnd.randrange(-100.0, 50.0, 10.0)], ro=[0, rnd.randrange(0.0, 360.0, 10.0), 0])
mc.xform(exec3, t=[rnd.randrange(-100.0, 50.0, 10.0), 0, rnd.randrange(-100.0, 50.0, 10.0)], ro=[0, rnd.randrange(0.0, 360.0, 10.0), 0])
mc.xform(exec4, t=[rnd.randrange(-100.0, 50.0, 10.0), 0, rnd.randrange(-100.0, 50.0, 10.0)], ro=[0, rnd.randrange(0.0, 360.0, 10.0), 0])

# for i in range(100):
#     i = xavierRocaCrespo_ex1('botBunny', smoothGeo=False)
#     mc.xform(i, t=[rnd.randrange(-100.0, 50.0, 10.0), 0, rnd.randrange(-100.0, 50.0, 10.0)],
#              ro=[0, rnd.randrange(0.0, 360.0, 10.0), 0])

mc.viewFit(all=True)

