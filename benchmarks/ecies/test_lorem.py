from lorem_text import lorem  # type: ignore
from parameterized import parameterized  # type: ignore

from crunch_encrypt.ecies import (decrypt_bytes, encrypt_bytes,
                                  generate_keypair_pem)

(
    private_key_pem,
    public_key_pem,
) = generate_keypair_pem()

max_count = 10 * 1024 + 10  # 10 KiB + 10 bytes
big_paragraph = lorem.COMMON_P.encode("utf-8") * 1000
assert len(big_paragraph) > max_count


@parameterized.expand([  # type: ignore
    (size,)
    for size in range(0, max_count)
])
def test_encrypt_decrypt(input_size: int):
    original = big_paragraph[:input_size]

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
