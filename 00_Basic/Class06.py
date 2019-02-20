import maya.cmds as mc

def listAttr():
    # cargar seleccion
    sel = mc.ls(sl=True)

    # la lista de los atributos que puedan tener key
    attrs = mc.listAttr(sel[0], keyable=True)

    return attrs

winID = 'windowXavi'

if mc.window(winID, exists = True):
    mc.deleteUI(winID)

window = mc.window(winID, title='Long Name', iconName='Short Name', widthHeight=(200,55))
mc.columnLayout(adjustableColumn=True)
slider = mc.floatSliderButtonGrp(label='Slider',
                        field=False,
                        buttonLabel='ALL',
                        symbolButtonDisplay=False,
                        columnWidth=(2,23))

attributes = listAttr()

attrSel = mc.iconTextScrollList(allowMultiSelection=False,
                                append=(attributes))

mc.floatSliderButtonGrp(slider, e=True, dragCommand='doKeyframe(slider,attrSel)')

mc.showWindow(window)


def sliderCanvia(widget):
    print mc.floatSliderButtonGrp(widget, q=True,value=True)

def doKeyframe(widget,attrSel):
    value = mc.floatSliderButtonGrp(widget, q=True, value=True)
    tween(value,attrSel)

def tween(prc = 50, attrSel = 'ALL'):
    #cargar seleccion
    sel = mc.ls(sl=True)

    #la lista de los atributos que puedan tener key
    attrs = attrSel
    
    #hacer for loop, at son atributos
    current = mc.currentTime(query=True)
    for at in attrs:
        currAttr = "{0}.{1}".format(sel[0],at)
        llista_kfs = mc.keyframe(currAttr, query=True) #mc.keyframe("obj.attribut", query=True)
        
        if llista_kfs == None:
            continue  #el continue obliga a hacer un salto, no como el return que para del todo
            
        #print at, llista_kfs
        
        #crear listas append para guardar kf anteriores y posteriores
        anteriors = []
        posteriors = []
        
        for kf in llista_kfs:
            if kf > current:
                posteriors.append(kf)
            elif kf < current:
                anteriors.append(kf)
        
        #print at
        #print "ANTERIORS:{}".format(anteriors)
        #print "POSTERIORS:{}".format(posteriors)
        if not anteriors or not posteriors:
            continue
        
        previ = max(anteriors)
        seguent = min(posteriors)
        #print "PREVI:{}".format(previ)
        #print "SEGUENT:{}".format(seguent)
        
        #con esto sabemos el valor del frame previo o siguiente
        valorPrevi = mc.getAttr(currAttr, time=previ)
        valorPosterior = mc.getAttr(currAttr, time=seguent)
    
        increment = valorPosterior - valorPrevi
        valorIn = valorPrevi + (prc/100.0) * increment #valorInbetween
        
        # print increment
        
        mc.setAttr(currAttr, valorIn)
        mc.setKeyframe(currAttr, time=current, value=valorIn)




























