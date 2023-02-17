from pywinauto import Application, keyboard, mouse, findwindows
import time

# app = Application(backend="uia").start(r'mmc devmgmt.msc') # mmc.exe spawns a child process
# app = Application(backend="uia").connect(path='mmc.exe') # connect to a child one
#
# '''
# The way Device Manager is opened causes a popup to display.  The popup states:
#     You are logged on as a standard user. You can view device settings in Device
#     Manager, but you must be logged on as an administrator to make changes.
# '''
# dlgBox = app.DeviceManager.child_window(title="OK", auto_id="2", control_type="Button").wrapper_object()
# dlgBox.click_input() # Click on the OK button
#
# menuView = app.DeviceManager.child_window(title="View", control_type="MenuItem").wrapper_object()
# menuView.click_input() # Clicks the View menu item
# keyboard.send_keys('w') # Press w to select Show hidden devices
'''
Keyboard notes > https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
Mouse notes > https://pywinauto.readthedocs.io/en/latest/code/pywinauto.mouse.html
'''
keyboard.send_keys("{LWIN down}" "r" "{LWIN up}") # Press the Winows key and R to open the Run dialog
keyboard.send_keys("devmgmt.msc" "{ENTER}") # Type devmgmt.msc into the Run dialog then press enter

'''
Right click Accessibility Insights for Windows and select Run Elevated with Defendpoint.
With Device Manager open, hover the mouse over the title bar.
Pause Live Inspect.
Select window 'Device Manager' to see all of its elements.
ProcessID = 23356, open Task Manager and look at Details, sort by PID.  23356 belongs to MMC.exe
ClassName = MMCMainFrame
Name = Device Manager
'''
className = 'MMCMainFrame'
name = 'Device Manager'

time.sleep(1) # wait 1 second to make sure window is open, without it was happening too fast and would sometimes error.
mywin = findwindows.find_window(active_only=True, class_name=className, title_re="Device Manager")
print("mywin = " + str(mywin)) # this is the handle for the window

app = Application(backend="uia").connect(handle=mywin)
print("app = " + str(app))

# Select View from the menu options then press the w key to select Show hidden devices
# menuView = app.DeviceManager.child_window(title="View", control_type="MenuItem")
# menuView.click_input() # Clicks the View menu item
# keyboard.send_keys('w') # Type w to select Show hidden devices

win = app.window(title_re='Device Manager')
print("win = " + str(win))

dlg = app['Device Manager']
print("dlg = " + str(dlg))

# Maximize the Device Managerwindow
# maxWindow = app.DeviceManager.child_window(title="Maximize", control_type="Button")
# maxWindow.click_input() # Click the maximize button

# mouse.click(button='left', coords=(787, 57))
# causing a RuntimeError: There is no active desktop required for moving mouse cursor!