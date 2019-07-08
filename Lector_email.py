import imaplib
import email


email2 = "nprueba1995@gmail.com"
passw = "rjucgllllvkanbxf"
smtp_server = "imap.gmail.com"
smtp_port = 993


def extract_body(payload):
    if isinstance(payload,str):
        return payload
    elif isinstance(payload,type(None)):
    	print("entre aquiii")
    elif isinstance(payload,int):
    	print("holo")
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

def leer_email():
	mail = imaplib.IMAP4_SSL(smtp_server, smtp_port)
	mail.login(email2,passw)
	mail.select('inbox')
	#typ, data = mail.search(None,'UNSEEN') son los mensaje que no he visto
	typ,data = mail.search (None,"ALL")
	ids = data[0]
	id_lista = ids.split()

	for element in id_lista:
		typ2,data2 = mail.fetch(element,'(RFC822)')
		#email_body = data2[0][1]
		#print(email.message_from_string(email_body.decode("utf-8")))
		for response in data2:
			if isinstance(response,tuple):
				#print(email.message_from_string((response[1].decode("utf-8"))))
				nico = email.message_from_bytes((response[1]))

				if nico.is_multipart():
					for part in nico.walk():
						payload = part.get_payload(decode = True)
						if payload == None:
							pass
						else:
							strtext = payload.decode()
							print(strtext)
							break
				else:
					payload = nico.get_payload(decode=True)
					if payload == None:
						pass
					else:
						strtext = payload.decode()
						print(strtext)
						break






if __name__ == "__main__":
	leer_email()


