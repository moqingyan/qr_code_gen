
from qrcodegen import QrCode, QrSegment

def print_qr(qrcode: QrCode) -> None:
	"""Prints the given QrCode object to the console."""
	border = 4
	for y in range(-border, qrcode.get_size() + border):
		for x in range(-border, qrcode.get_size() + border):
			print("\u2588 "[1 if qrcode.get_module(x,y) else 0] * 2, end="")
		print()
	print()


def do_demo(url_string) -> None:
	"""Creates a variety of QR Codes that exercise different features of the library, and prints each one to the console."""
	
	# Numeric mode encoding (3.33 bits per digit)
	segs = QrSegment.make_segments(url_string)
	qr = QrCode.encode_segments(segs, QrCode.Ecc.HIGH, mask=-1)  # Automatic mask
	print_qr(qr)
	
	
if __name__ == "__main__":
	url_string = 'https://www.scallop-lang.org'
	do_demo(url_string)