\\.\COM7 properties
	Max output buffer size: no limit
	Max input buffer size: no limit
	Current output buffer size: unavailable
	Current input buffer size: 16384
	Max baud rate: user programmable
	Provider subtypes:
		PARALLELPORT
		RS422
		RS423
		RS449
		MODEM
		SCANNER
		TCPIP_TELNET
		X25
	Provider capabilities:
		DTRDSR
		RLSD
		PARITY_CHECK
		TOTALTIMEOUTS
		INTTIMEOUTS
	Settable parameters:
		PARITY
		BAUD
		DATABITS
		STOPBITS
		HANDSHAKING
		PARITY_CHECK
		RLSD
	Settable baud rates:
		300
		600
		1200
		2400
		4800
		9600
		19200
		38400
		57600
		115200
	Settable user baud rates: False
	Settable data bits:
		7
		8
	Settable wide data bits: False
	Settable stop bits:
		1
	Settable parity:
		NONE
		ODD
		EVEN
		MARK
		SPACE

Process finished with exit code 0
