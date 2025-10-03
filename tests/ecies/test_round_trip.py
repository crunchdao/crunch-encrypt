from crunch_encrypt.ecies import (decrypt_bytes, encrypt_bytes,
                                  generate_keypair_pem)

(
    private_key_pem,
    public_key_pem,
) = generate_keypair_pem()


def test_encrypt_decrypt():
    original = b"Hello World!"

    (
        encrypted,
        ephemeral_public_key_pem,
    ) = encrypt_bytes(
        original,
        public_key_pem=public_key_pem,
    )

    decrypted = decrypt_bytes(
        encrypted,
        private_key_pem=private_key_pem,
        ephemeral_public_key_pem=ephemeral_public_key_pem,
    )

    assert original == decrypted
