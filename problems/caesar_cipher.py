k = 3
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = int(input("1. Encrypt\n2. Decrypt\n3. Exit\n"))

if x == 1:
    print("Encrypt")
    text1 = input("Enter the text: ").upper()
    encoded_text = ""
    for ch in text1:
        if ch in alphabets:
            num = alphabets.find(ch)
            num = (num + k) % len(alphabets)
            encoded_text = encoded_text + alphabets[num]
        else:
            encoded_text = encoded_text + ch
    print("Encrypted text:", encoded_text)
if x == 2:
    print("Decrypt")
    text2 = input("Enter the text: ").upper()
    decoded_text = ""
    for ch in text2:
        if ch in alphabets:
            num = alphabets.find(ch)
            num = (num - k) % len(alphabets)
            decoded_text = decoded_text + alphabets[num]
        else:
            decoded_text = decoded_text + ch
    print("Decrypted text:", decoded_text)
else:
    exit(0)
