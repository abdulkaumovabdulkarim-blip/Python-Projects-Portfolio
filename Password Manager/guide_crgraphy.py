from cryptography.fernet import Fernet

# 1. Генерация ключа (его нужно сохранить в секрете!)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# 2. Загрузка ключа
cipher_suite = Fernet(key)

# 3. Шифрование данных (данные должны быть в байтах)
message = "Конфиденциальная информация".encode()
cipher_text = cipher_suite.encrypt(message)
print(f"Зашифровано: {cipher_text}")

# 4. Расшифровка
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Расшифровано: {plain_text.decode()}")


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. Генерация пары ключей
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 2. Шифрование публичным ключом
message = b"Secret for RSA"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 3. Расшифровка приватным ключом
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"RSA результат: {plaintext.decode()}")

from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"my message")
digest.update(b" more data") # Можно добавлять данные частями
hash_result = digest.finalize()

print(f"Хеш (hex): {hash_result.hex()}")

import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

password = b"user_password_123"
salt = b'\x00' * 16  # В реальном проекте используйте os.urandom(16)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

token = f.encrypt(b"Data protected by password")
print(f"Зашифровано паролем: {token}")




# PROGRAM EXAMPLE ----

import os
from cryptography.fernet import Fernet

# Имена файлов для хранения данных
KEY_FILE = "master.key"
DATA_FILE = "user_code.bin"

def load_or_create_key():
    """Загружает существующий ключ или создает новый при первом запуске."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

def save_user_code(code, cipher_suite):
    """Шифрует и сохраняет код пользователя в файл."""
    encrypted_code = cipher_suite.encrypt(code.encode())
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted_code)
    print("✅ Код успешно зашифрован и сохранен!")

def show_user_code(cipher_suite):
    """Считывает, расшифровывает и показывает код."""
    if not os.path.exists(DATA_FILE):
        print("❌ Сохраненных кодов не найдено.")
        return

    with open(DATA_FILE, "rb") as f:
        encrypted_code = f.read()
    
    decrypted_code = cipher_suite.decrypt(encrypted_code)
    print(f"🔓 Ваш сохраненный код: {decrypted_code.decode()}")

def main():
    # 1. Подготавливаем шифровальщик
    key = load_or_create_key()
    cipher_suite = Fernet(key)

    while True:
        print("\n--- Менеджер Секретных Кодов ---")
        print("1. Сохранить новый код")
        print("2. Показать мой код")
        print("3. Выход")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            user_code = input("Введите код, который хотите спрятать: ")
            save_user_code(user_code, cipher_suite)
        elif choice == "2":
            show_user_code(cipher_suite)
        elif choice == "3":
            break
        else:
            print("Неверный ввод, попробуйте еще раз.")

if __name__ == "__main__":
    main()
