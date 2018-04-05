# files tracked: i3, polybar, rofi, vimrc, zshrc, xresources
# i3 - /home/rusty/.config/i3/config
# polybar - /home/rusty/.config/polybar/config

import hashlib

hash1 = hashlib.md5(open("/home/rusty/test",'rb').read()).hexdigest()

hash2 = hashlib.md5(open("/home/rusty/test2",'rb').read()).hexdigest()

if hash1 != hash2:
    print("The files are different.")
elif hash1 == hash2:
    print("The files are the same")