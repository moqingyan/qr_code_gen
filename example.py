
from qrcodegen import QrCode, QrSegment
import os

def print_qr(qrcode: QrCode) -> None:
	"""Prints the given QrCode object to the console."""
	border = 4
	for y in range(-border, qrcode.get_size() + border):
		for x in range(-border, qrcode.get_size() + border):
			print("\u2588 "[1 if qrcode.get_module(x,y) else 0] * 2, end="")
		print()
	print()

def to_svg_str(qr: QrCode, border: int) -> str:
	"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
	of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
	if border < 0:
		raise ValueError("Border must be non-negative")
	parts: List[str] = []
	for y in range(qr.get_size()):
		for x in range(qr.get_size()):
			if qr.get_module(x, y):
				parts.append(f"M{x+border},{y+border}h1v1h-1z")
	return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""

def do_demo(url_string, save_path) -> None:
	"""Creates a variety of QR Codes that exercise different features of the library, and prints each one to the console."""
	
	# Numeric mode encoding (3.33 bits per digit)
	segs = QrSegment.make_segments(url_string)
	qr = QrCode.encode_segments(segs, QrCode.Ecc.HIGH, mask=-1)  # Automatic mask
	svg = to_svg_str(qr, 2)
	with open(save_path, 'w') as file:
		file.write(svg)
	
	
if __name__ == "__main__":
	url_string = 'https://www.scallop-lang.org/blog/aaai24.html'
	save_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../output'))
	save_path = os.path.join(save_dir, 'res.svg')
	do_demo(url_string, save_path)