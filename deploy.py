import os

def wlDeploy(username, password, adminURL, appName, appPath):
    try:
        #connect to admin server
        connect(username, password, adminURL)

        #start edit operation
        edit()
        startEdit()

        #start deploying application to admin server
        progress = deploy(appName,appPath,targets="managed_1",upload='true')
        progress.printStatus()
        save()
        activate(20000,block="true")
        startApplication(appName)
        #disconnect from Admin server
        disconnect()
        exit()
    except Exception, ex:
        print ex.toString()
        cancelEdit('y')

wlDeploy("weblogic","welcome1","t3://127.0.0.1:7001","myApp", "/home/centos/ansible-weblogic/sample.war")
#wlDeploy("<Admin User Name>","<Password>","<AdminUrl","<App Name>", "<Path of war file>")
