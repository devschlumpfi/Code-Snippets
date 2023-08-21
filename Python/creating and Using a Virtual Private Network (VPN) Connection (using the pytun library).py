from pytun import TunTapDevice

tun = TunTapDevice(name="mytun")
tun.addr = "10.0.0.1"
tun.netmask = "255.255.255.0"
tun.up()
