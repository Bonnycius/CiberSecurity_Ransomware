import os
import pyaes

## abrir o arquivo criptografado
file_name = "Teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"#qualquer$senha#" ## 16 caractéres de senha / deve ser a mesma do arquivo encrypter.py
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "Teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
