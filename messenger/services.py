from .models import Message
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from django.utils import timezone
from datetime import timedelta
import environ
import os

# Set env for key usage.
# To use a different env file, run `ENV_PATH=other-env ./manage.py runserver`
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'Runar', env.str('ENV_PATH', '.env')))
DEFAULT_KEY = env.str('DEFAULT_KEY')


# Purpose:  encrypts and saves a message
# @params:  message: string = the real message we want to encrypt
#           key: string = the fake message used in decryption process
# @returns: Message (used for URL generation to redeem by recipient)
def encrypt_message(message, key):
    dust_up_the_olds()  # first look for old records and delete them
    default_key_used = 0
    if not key:
        key = DEFAULT_KEY
        default_key_used = 1
    iv = get_random_bytes(16)
    key = handle_up_key(key)
    message = message.encode()
    message = message + (AES.block_size - (len(message) % AES.block_size)) * b'\x00'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    coded = cipher.encrypt(message)
    m = Message(ciphertext=coded, identifier=iv, default_key=default_key_used)
    m.save()
    return m


# Purpose:  looks up the default_key value for a message identifier
# this determines whether or not a default key was used for encryption
# @params:  identifier: string = a string representing a byte array id field of message
# @returns: default_key: boolean = the value of the default_key for a message
def lookup_default_key(identifier):
    identity = bytearray.fromhex(identifier)
    m = Message.objects.get(identifier=identity)
    return m.default_key


# Purpose:  finds a message and decrypts it
# @params:  identifier: binary = used to find the message to decrypt
#           up_key: string = user provided key for decryption to decipher message
# @returns: String (recipient's decoded message)
def decrypt_message(identifier, up_key):
    identifier = bytearray.fromhex(identifier)
    if not up_key:
        up_key = DEFAULT_KEY
    dust_up_the_olds()  # first, look for any old records and delete them
    m = Message.objects.get(identifier=identifier)  # then work to get message
    message = m.ciphertext
    iv = m.identifier
    key = handle_up_key(up_key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decoded = cipher.decrypt(message)
    destroy_message(m)  # after message is found and decrypted, delete from db
    return decoded.decode('UTF-8')


# Purpose:  takes a user provided key as a string and formats it properly
# @params:  up_key: string = user provided string as key for decryption
# @returns: Binary (key for with to encrypt and decrypt)
def handle_up_key(up_key):
    key = up_key.strip()  # remove whitespaces
    key = key.encode()
    key = key + (AES.block_size - (len(key) % AES.block_size)) * b'\x00'
    key = key[:32]  # trim key down to a usable size of 32
    return key


# Purpose:  takes a message object and destroys it forever.
# @params:  message: Message = message object that has just been received
# @returns: null
def destroy_message(message):
    message.delete()
    return


# Purpose:  looks for messages older than 24 hrs, and destroys them forever.
# @params:  none
# @returns: null
def dust_up_the_olds():
    time_threshold = timezone.now() - timedelta(days=1)
    try:
        olds = Message.objects.filter(created_at__lt=time_threshold)
        olds.delete()
    finally:
        return
