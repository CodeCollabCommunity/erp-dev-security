from Crypto.PublicKey import RSA


key = RSA.generate(bits=2048)

private_key = key.export_key(format='PEM')
public_key = key.public_key().export_key(format='PEM')

with open('erp_private_key.pem', 'wb') as f:
    f.write(private_key)

with open('erp_public_key.pem', 'wb') as f:
    f.write(public_key)
