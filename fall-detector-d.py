import android
import time
droid = android.Android()
droid.startSensingTimed(1,50)


def onFall():
 droid.stopSensing()
 droid.dialogCreateAlert("Fall Detection","You are falling")
 droid.dialogSetPositiveButtonText("OK")
 droid.dialogShow()


time.sleep(1)
i=0
axis =0
while 1:
 x = droid.readSensors().result['xforce']
 y = droid.readSensors().result['yforce']
 z = droid.readSensors().result['zforce']
 if x > 8 and x < 12:
  axis = 'x'
 elif y > 8 and y < 12:
  axis = 'y'
 elif z > 8 and z < 12:
  axis = 'z'
 print axis
 if axis =='z' and z>15:
  print "falling"
  onFall()
  break
 elif axis =='y' and y>15:
  print "falling"
  onFall()
  break
 elif axis =='x' and x>15:
  print "falling"
  onFall()
  break

 time.sleep(0.1)
 