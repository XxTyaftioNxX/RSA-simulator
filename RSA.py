
'''
File containing necessary funtions for RSA
get_random_primes, is_prime, modular_inverse, generate_key_pair, encrypt, decrypt
'''

#Generating random prime number
from sympy import randprime
from math import gcd
import random 

#Get random primes if user chooses not to input
def get_random_primes():
    return randprime(1, 9999999), randprime(1, 9999999) 
    
#Check if user input numbers are prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

#used to find the private exponent(d)
def modular_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

#generating public and private key pairs
def generate_key_pair(prime1, prime2):
    if not (is_prime(prime1) and is_prime(prime2)):
        raise ValueError('Both numbers must be prime.')
    elif prime1 == prime2:
        raise ValueError('prime1 and prime2 cannot be equal')

    # n = pq
    n = prime1 * prime2

    # ʎ is the totient of n
    phi = (prime1-1) * (prime2-1)


    #choosing the public exponent such that 1 < e < ʎ(n) and gcd(e, ʎ(n)) = 1

    e = random.randrange(1, phi)

    # verifying that e and ʎ(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)


    # Use Extended Euclid's Algorithm to generate the private key
    d = modular_inverse(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    public_key, n = pk
    # encrypt each letter in the plaintext based on the character using m^e mod N
    ciphertext = [pow(ord(char), public_key, n) for char in plaintext]
    # Return the array of bytes
    return ciphertext

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    private_key, n = pk
    # Decrypting the plaintext based on the ciphertext and key using c^d mod N
    aux = [str(pow(char, private_key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)





