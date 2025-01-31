import bge.logic as logic
import os
import json
import copy
utils = logic.utils
cont = logic.getCurrentController()
own = cont.owner
scene = logic.getCurrentScene()
blendPath = logic.expandPath("//")
def main():
    #if logic.finishedLastLap:
    saveMapToFile(logic.ghosts,"ghost.json")
        
def saveMapToFile(ghosts,fileName):
    fileName = blendPath+"ghosts"+os.sep+fileName
    logic.utils.log("saving ghost: "+fileName)
    print("saving ghost to: "+fileName)
    ghostContent = {"map":logic.utils.gameState["selectedMap"],"sessionRecording":[]}
    with open(fileName, 'w+') as saveFile:
        for i in range(0,len(ghosts)):
            gObj = ghosts[i]['obj'].name
            gFrames = ghosts[i]['frames']
            ghostContent["sessionRecording"].append({"obj":gObj,"frames":gFrames}) #let's keep everything serializable 
        
        saveFile.write(str(json.dumps(ghostContent)))
        saveFile.close()
    #except Exception as e:
    #    logic.utils.log("ghost save error: "+str(e))
    logic.utils.log("ghost save complete: "+fileName)
        
main()