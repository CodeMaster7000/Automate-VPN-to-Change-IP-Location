import os
import random
from time import sleep

codeList = ["TR", "US-C", "US", "US-W", "CA-W", "FR", "DE", "NL", "NO", "RO", "CA", "CH", "GB", "HK"]

try:
	os.system("Windscribe connect")
	while True:
		choiceCode = random.choice(codeList)
		sleep(random.randrange(120, 300))
		print("Changing IP address...")
		os.system("Windscribe connect " + choiceCode)

except:
	os.system("Windscribe disconnect")
	print("An unexpected error occurred.")
