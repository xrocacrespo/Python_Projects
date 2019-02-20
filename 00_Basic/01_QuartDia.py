import maya.cmds as mc

winID = 'windowXavi'

if mc.window(winID, exists = True):
    mc.deleteUI(winID)

window = mc.window(winID, title='Long Name', iconName='Short Name', widthHeight=(200,55))
mc.columnLayout(adjustableColumn=True)
slider = mc.floatSliderButtonGrp(label='Slider',
                        field=True,
                        buttonLabel='Button',
                        symbolButtonDisplay=False,
                        columnWidth=(5,23),
                        image='cmdWndIcon.xpm')

mc.floatSliderButtonGrp(slider, e=True, cc='sliderCanvia(slider)')
row = mc.rowLayout(nc=2)
mc.button(label='Do nothing')
mc.button(label = 'Close', command=('mc.deleteUI("{0}", window=True)').format(window))

mc.setParent("..")
mc.button('tercer Boto')

mc.showWindow(window)

def sliderCanvia(widget):
    print mc.floatSliderButtonGrp(widget, q=True,value=True)
