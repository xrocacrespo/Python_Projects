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


# Creacio de les orelles
def creacioOrelles():
    ears=[]
    for side in ['L','R']:
        name_geo = '{}_earBotBunny_geo'.format(side)
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
        ear_connection = mc.polyCube(name='{}_earConnectionBotBunny_geo'.format(side), w=0.7, h=2, d=0.7, sw=5, sh=5, sd=5)
        mc.move(0, -3.5, 0, ear_connection)

        # Shading
        createMats(ear[0], 'phong', 0.238, 0, 0)
        createMats(ear_connection[0], 'phong', 0.12, 0.12, 0.12)

        # Grouping
        mc.select(ear[0], ear_connection[0])
        ear_grp = mc.group(name= name_geo + '_grp')
        ears.append(ear_grp)
    l_ear=ears[0]
    r_ear=ears[1]

    # POSITION AND SCALE
    mc.scale(-1.345, 1.345, 1.345, r_ear)
    mc.move(4.232, 26.36, -3.592, r_ear)
    mc.rotate(-21.168, 7.997, -29.047, r_ear)
    mc.scale(1.345, 1.345, 1.345, l_ear)
    mc.move(-4.232, 26.36, -3.592, l_ear)
    mc.rotate(-21.168, -7.997, 29.047, l_ear)

# Creacio del cap
def creacioCap():
    name_geo = 'C_headBotBunny_geo'
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
    eyes = mc.polyCube(n='C_eyesBotBunny_geo', sw=2, sh=2, sd=2)
    mc.xform(eyes[0], t=[0,21.234,3.785], ro=[-11.618,0,0], s=[6.136,2.055,1.653])
    mc.select('{}.f[0:3]'.format(eyes[0]))
    mc.polyExtrudeFacet(thickness=0, scale=[0.9, 0.9, 0.9])
    mc.polyExtrudeFacet(thickness=0, scale=[0.9, 0.9, 0.9])
    mc.polyExtrudeFacet(thickness=-0.2)
    mc.polyExtrudeFacet(thickness=-0.2)

    # Shading
    createMats(head[0], 'phong', 1, 1, 1)
    createMats(eyes[0], 'phong', 0.12, 0.12, 0.12)
    mc.select('{}.f[48:55]'.format(eyes[0]), '{}.f[0:3]'.format(eyes[0]))
    mc.sets(e = True, forceElement='R_earBotBunny_geo_phongSG')

    # Grouping
    head_grp = mc.group(n='C_headBotBunny_grp', em=True)
    mc.parent(head[0], eyes[0], head_grp)


# Creacio del body
def creacioBody():
    name_geo = 'C_bodyBotBunny_geo'
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
    createMats(body[0], 'phong', 1, 1, 1)

    # COLL
    coll = mc.polyCube(name='C_neckBotBunny_geo', sw=2, sh=2, sd=2)
    mc.move(0,13.623,0, coll[0])

    # Shading
    createMats(coll[0], 'phong', 0.12, 0.12, 0.12)


    # Grouping
    body_grp = mc.group(n='C_bodyBotBunny_grp', em=True)
    mc.parent(body[0], coll[0], body_grp)

# Creacio dels Arms
def creacioArms():
    arms = []
    for side in ['L','R']:
        arm_part1 = mc.polyCube(n='{}_arm01BotBunny_geo'.format(side), w=2, h=4, d=2, sh=2, sd=2, sw=3)
        mc.select(arm_part1[0] + '.f[1]',arm_part1[0] + '.f[22]')
        mc.scale(1.5,1,1, r=True)
        mc.polyExtrudeFacet(thickness=-0.4)
        mc.polyExtrudeFacet(thickness=-0.4)
        mc.move(0, 2, 0, arm_part1[0])

        arm_part2 = mc.polySphere(n='{}_arm02BotBunny_geo'.format(side), sa=6, sh=6)
        mc.move(0,0,0.889, arm_part2[0])
        mc.scale(1, 2.522, 1, arm_part2[0])

        arm_part3 = mc.duplicate(arm_part1[0], n='{}_arm03BotBunny_geo'.format(side))
        mc.move(-0.027, -2.777, 0.67, arm_part3)
        mc.rotate(-33.848, 0, 0, arm_part3)
        mc.scale(1, -1, 1, arm_part3)

        #HAND
        arm_part4 = mc.polyCube(n='{}_hand01BotBunny_geo'.format(side), sw=3, sh=3, sd=3)
        mc.move(-0.279, -5.082, 2.266, arm_part4[0])
        mc.rotate(-34.836, 0, 0, arm_part4[0])
        mc.scale(0.775, 1.354, 1.445, arm_part4[0])
        mc.move(0,0.148768,0, arm_part4[0]+'.f[12:14]', r=True )

        arm_part5 = mc.polyCube(n='{}_hand02BotBunny_geo'.format(side), sw=3, sh=3, sd=3)
        mc.move(0.49, -4.837, 2.105, arm_part5[0])
        mc.rotate(-37.317, 0, 0, arm_part5[0])
        mc.scale(0.473, 1, 1, arm_part5[0])

        # Shading
        createMats(arm_part1[0], 'phong', 1, 1, 1)
        createMats(arm_part2[0], 'phong', 0.12, 0.12, 0.12)
        createMats(arm_part3[0], 'phong', 1, 1, 1)
        createMats(arm_part4[0], 'phong', 0.12, 0.12, 0.12)
        createMats(arm_part5[0], 'phong', 0.12, 0.12, 0.12)

        arm_group = mc.group(
            arm_part1[0],
            arm_part2[0],
            arm_part3[0],
            arm_part4[0],
            arm_part5[0],
            n='{}_armBotBunny_grp'.format(side))
        arms.append(arm_group)

        # JUNTES
        arm_part6 = mc.polyCylinder(n='{}_junta01BotBunny_geo'.format(side), sa=12, sh=3, sc=2)
        mc.xform(arm_part6[0], s=[0.389, 1.565, 0.389], t=[0.286, 3.178, 0.044], ro=[0, 0, -90])
        mc.parent(arm_part6[0], arm_group)

        # Shading
        createMats(arm_part6[0], 'phong', 0.12, 0.12, 0.12)

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
def creacioLegs():
    legs = []
    for side in ['L', 'R']:
        leg_part1 = mc.polyCube(n='{}_leg01BotBunny_geo'.format(side), w=3.5, h=3.5, d=3.5, sh=2, sw=3)
        mc.scale(0.526, 1.939, 0.961, leg_part1[0])
        mc.move(-2.07, 3.346, 1.48, leg_part1[0])
        mc.select(leg_part1[0]+'.vtx[4:7]', leg_part1[0]+'.vtx[16:19]')
        mc.move(0, 0.4, 0.8, r=True)
        mc.scale(1, 1.5, 1.5)
        mc.select(leg_part1[0] + '.vtx[16:19]')
        mc.move(0, 0, 1.7, r=True)
        mc.select(leg_part1[0] + '.vtx[0:3]', leg_part1[0] + '.vtx[20:23]')
        mc.scale(0.5, 1, 0.6)

        leg_part2 = mc.polyCube(n='{}_leg02BotBunny_geo'.format(side), sw=2, sh=2, sd=3)
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
        leg_part3 = mc.polyCylinder(n='{}_junta02BotBunny_geo'.format(side), sa=12, sh=3, sc=2)
        mc.xform(leg_part3[0], s=[0.736, 1.565, 0.736], t=[-1.632, 5.52, 1.879], ro=[0, 0, -90])

        # Shading
        createMats(leg_part1[0], 'phong', 1, 1, 1)
        createMats(leg_part2[0], 'phong', 1, 1, 1)
        createMats(leg_part3[0], 'phong', 0.12, 0.12, 0.12)
        mc.select('{}.f[6:19]'.format(leg_part2[0]), '{}.f[20:21]'.format(leg_part2[0]), '{}.f[23:24]'.format(leg_part2[0]), '{}.f[26:27]'.format(leg_part2[0]), '{}.f[29:30]'.format(leg_part2[0]), '{}.f[34:35]'.format(leg_part2[0]), '{}.f[37:38]'.format(leg_part2[0]), '{}.f[40:41]'.format(leg_part2[0]))
        mc.sets(e=True, forceElement='R_earBotBunny_geo_phongSG')

        leg_grp = mc.group(em=True, n='{}_legBotBunny_grp'.format(side))
        mc.parent(leg_part1[0], leg_part2[0], leg_part3[0], leg_grp)
        legs.append(leg_grp)

        if side == 'R':
            mc.scale(-1, 1, 1, leg_grp)
            mc.move(1, 0, 0, leg_grp)
        else:
            mc.move(-1, 0, 0, leg_grp)

# Creacio del la Cua
def creacioCua():
    cua = mc.polySphere(n='C_tailBotBunny_geo', sa=10, sh=10, r=2)
    mc.move(0,4.197,-2.285, cua[0])

    # Shading
    createMats(cua[0], 'lambert', 1, 1, 1)



# GROUP AND REPOSITION
def groupAndReposition():
    mc.select('*_geo')
    all_geo = mc.ls(selection=True, type='transform')
    mc.select(all=True)
    global_grp= mc.group(n='Bot_Bunny_GRP')
    mc.move(0, 3, 0, global_grp)
    mc.rotate(10.243,0,0, global_grp)


# SMOOTH ALL
def smoothAll(var):
    # SMOOTH FOR ALL GEO
    if var == 'si':
        for obj in all_geo:
            mc.polySmooth(obj)
    else:
        mc.displaySmoothness(po=3)


# BUILD
newFile()
creacioOrelles()
creacioCap()
creacioBody()
creacioArms()
creacioLegs()
creacioCua()
groupAndReposition()
smoothAll('no')
mc.viewFit(all=True)

