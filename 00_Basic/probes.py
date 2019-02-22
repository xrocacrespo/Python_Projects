winID = 'windowXavi'

        if mc.window(winID, exists=True):
            mc.deleteUI(winID)

        window = mc.window(winID, title='{} Settings'.format(moduleName), iconName='Short Name', resizeToFitChildren=True)
        colLay = mc.columnLayout('colLayout1', adjustableColumn=True)
        mc.text(l='')

        mc.text('STEPS')
        fieldnameStep = mc.textFieldGrp('fieldnameStep', l='Name step', cal=[1,'right'], tx='step')
        fieldnumSteps = mc.intSliderGrp('fieldnumSteps', l='Number Steps', cal=[1, 'right'], v=20, f=True, fieldMaxValue=100, maxValue=50)
        fieldwidthStep = mc.floatSliderGrp('fieldwidthStep', l='Width', cal=[1, 'right'], v=5, f=True, fieldMaxValue=100, maxValue=10)
        fieldheightStep = mc.floatSliderGrp('fieldheightStep', l='Height', cal=[1, 'right'], v=0.2, f=True, fieldMaxValue=100, maxValue=10)
        fielddepthStep = mc.floatSliderGrp('fielddepthStep', l='Depth', cal=[1, 'right'], v=2.0, f=True, fieldMaxValue=100, maxValue=10)
        fieldoffsetStep = mc.floatSliderGrp('fieldoffsetStep', l='Offset Y', cal=[1, 'right'], v=0.5, f=True, fieldMaxValue=100, maxValue=10)
        fieldradius = mc.floatSliderGrp('fieldradius', l='Radius', cal=[1, 'right'], v=2.0, f=True, fieldMaxValue=100, maxValue=10)
        fielddegrees = mc.floatSliderGrp('fielddegrees', l='Degrees', cal=[1, 'right'], v=10.0, f=True, fieldMaxValue=359.99, fieldMinValue=-359.99, maxValue=359.99, minValue=-359.99)
        mc.text(l='')

        mc.text('HAND BAR')
        mc.rowLayout(nc=2)
        mc.text(l='                                                                     ')
        fieldcreateHandBar = mc.checkBoxGrp('fieldcreateHandBar', l='Hand Bar      ', v1=True, cal=[2, 'right'])
        mc.setParent("..")
        fieldheightHandBar = mc.textFieldGrp('fieldheightHandBar', l='Height', cal=[1, 'right'], tx='4')
        fieldradiusHandBar = mc.textFieldGrp('fieldradiusHandBar', l='Radius', cal=[1, 'right'], tx='0.2')
        mc.text(l='')

        mc.text('UP BARS')
        fieldradiusUpBars = mc.textFieldGrp('fieldradiusUpBars', l='Radius', cal=[1, 'right'], tx='0.1')
        mc.text(l='')

        mc.text('SPHERES')
        fieldradiusHandleSpheres = mc.textFieldGrp('fieldradiusHandleSpheres', l='Radius', cal=[1, 'right'], tx='1')
        mc.text(l='')

        mc.text('CENTER COLUMN')
        mc.rowLayout(nc=2)
        mc.text(l='                                                                     ')
        fieldcreateCenterCol = mc.checkBoxGrp('fieldcreateCenterCol', l='Center Column    ', v1=True, cal=[2, 'right'])
        mc.setParent("..")
        mc.text(l='')
        mc.text(l='')

        createButton = mc.button(label='Create Stairs', command=('redoSettings()'))

        mc.checkBoxGrp(fieldcreateHandBar, e=True, ofc='apagarHandBar()', onc='encenderHandBar()')

        mc.showWindow(window)