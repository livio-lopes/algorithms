from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("bode", "cabra")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(["Bode", "Cabra"], 4)
    assert encrypt_message("batata", 3) == "tab_ata"
    assert encrypt_message("batata", 4) == "at_atab"
    assert encrypt_message("bode", 5) == "edob"
