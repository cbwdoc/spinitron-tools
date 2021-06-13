cont = ''
while cont.lower() != 'n':
	img = str(raw_input("Image?\n"))
	alt = str(raw_input("Alt text?\n"))
	notes = str(raw_input("Notes?\n"))
	bandcamp = str(raw_input("Bandcamp?\n"))
	purchase = str(raw_input("Purchase link?\n"))

	html = '<img src="%s" alt="%s" style="max-height:250px;"/>\n<p>%s</p>\n<p><a href="%s">Bandcamp</a> | <a href="%s">Vinyl</a></p>' % (img, alt, notes, bandcamp, purchase)
	print(html)

	cont = str(raw_input("Continue? (y/n)\n"))