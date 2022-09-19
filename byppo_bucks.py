import pyautogui
import time
# This code has the purpose of checking into byppo every two hours 
# in order to get the maximum amount of check-ins possible in a day
# Hope this works
print(pyautogui.size());

#mouse position for checkin = 258, 378


# Robot workflow - Angel Lopez Pol 9/18/2022

#Click on check in button
# Wait 15 seconds for check in to complete
# Click the same location to remove the check in confirmation
# Wait two hours an 1 minute
# Repeat first step
check_in_count = 0;
while True:
    pyautogui.moveTo(258, 378)
    pyautogui.click()
    check_in_count = check_in_count + 1
    time.sleep(15)
    pyautogui.click();
    time.sleep(60*60*2 + 3)