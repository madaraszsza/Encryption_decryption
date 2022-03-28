import unittest

alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "abcdefgijkl"
key2 = "grbqzcyzwgmtyabchzmdefghqst"
message = "helloworld"


def encrypt(message, key) -> str:
    encrypted_message = ""

    for i, k in zip(message, key):
        m_index = alphabet.find(i)
        k_index = alphabet.find(k)
        sum = m_index + k_index
        code = ""
        if sum > 26:
            code = alphabet[sum % 27]
        else:
            code = alphabet[sum]
        encrypted_message = encrypted_message + code
    return encrypted_message


def decrypt(encrypted_message, key) -> str:
    message = ""

    for i, k in zip(encrypted_message, key):
        em_index = alphabet.find(i)
        k_index = alphabet.find(k)
        diff = em_index - k_index
        code = ""
        if diff < 0:
            code = alphabet[diff + 27]
        else:
            code = alphabet[diff]
        message = message + code
    return message


a = encrypt(message, key)
print("A titkosított szöveg:", a)
print("A visszafejtett szöveg:", decrypt(a, key))

first_message = "early bird catches the worm"
second_message = "curiosity killed the cat"

encrypted_f_m = encrypt(first_message, key2)
encrypted_s_m = encrypt(second_message, key2)


def get_key_shard(encrypted_message, message) -> str:
    key_shard = ""

    for i, k in zip(encrypted_message, message):
        em_index = alphabet.find(i)
        m_index = alphabet.find(k)
        diff = em_index - m_index
        code = ""
        if diff < 0:
            code = alphabet[diff + 27]
        else:
            code = alphabet[diff]
        key_shard = key_shard + code
    return key_shard


m_shard = "early "
key = ""
key_length = 0
messages = [encrypted_f_m, encrypted_s_m]
words = ["early", "bird", "catches", "the", "worm", "curiosity", "killed", "cat"]
while len(key) < len(encrypted_f_m):
    key_shard = get_key_shard(messages[0][key_length:key_length + len(m_shard)], m_shard)
    d_s_m_shard = decrypt(messages[1][key_length:key_length + len(m_shard)], key_shard)
    key += key_shard
    key_length += len(key_shard)
    tmp_words = [string for string in words if d_s_m_shard in string]
    if len(tmp_words) > 0:
        if len(tmp_words[0]) > len(d_s_m_shard):
            m_shard = tmp_words[0][-(len(tmp_words[0]) - len(d_s_m_shard)):] + " "
        elif len(tmp_words[0]) == len(d_s_m_shard):
            m_shard = " "
        else:
            m_shard = tmp_words[0] + " "
    # print(m_shard)
    # print(d_s_m_shard)
    messages.reverse()
print(key)


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.message = "helloworld"
        self.key = "abcdefgijkl"

    def test_decrypt(self):
        encryptedMessage = encrypt(self.message, self.key)
        decryptedMessage = decrypt(encryptedMessage, self.key)
        self.assertEqual(decryptedMessage, self.message)


if __name__ == '__main__':
    unittest.main()
