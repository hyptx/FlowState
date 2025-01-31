import bge
logic = bge.logic
scene = logic.getCurrentScene()
cont = logic.getCurrentController()
owner = cont.owner
newCam = None
profileIndex = logic.globalDict['currentProfile']
profiles = logic.globalDict['profiles']
shaders = profiles[profileIndex]['graphicsSettings']['shaders']
for object in scene.objects:
    if object != owner:
        if "cameraName" in object:
            print("object "+str(object.name)+" has property 'cameraName'")
            if object['cameraName'] == owner['cameraName']:
                print("name matches!")
                newCam = object
                break
if newCam != None:
    print(newCam)
    scene.active_camera = newCam
    if(newCam == "mainCamera"):
        if(shaders):
            
            logic.sendMessage("enable shaders")
    else:
        if "FPV" not in str(newCam['cameraName']):
            logic.sendMessage("disable shaders")
        else:
            if(shaders):
                newCam.lens=5.823523998260498
                logic.sendMessage("enable shaders")
            else:
                newCam.lens=10