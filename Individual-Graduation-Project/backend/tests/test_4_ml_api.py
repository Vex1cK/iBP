from httpx import AsyncClient
import os

from .config_for_tests import PATH_TO_TEST_FILES
from .utils_for_tests import verify_users_email

async def test_access_to_models(ac: AsyncClient):
    ok = await verify_users_email("user1@example.com")
    assert ok
    register_response = await ac.post("/auth/login", json={"email": "user1@example.com", "password": "password123"})
    access_token = register_response.json()["access_token"]
    
    audio_file_path = os.path.join(PATH_TO_TEST_FILES, "test_audio_1.wav")
    
    with open(audio_file_path, "rb") as audio_file:
        files = {"file": ("test_audio_1.wav", audio_file, "audio/wav")}
        params = {"access_token": access_token}
        response = await ac.post("/ml/transcribe_audio", params=params, files=files)
    
    assert response.status_code == 200
    response_file_content = response.content
    assert response_file_content, "The response file is empty"

    response_path = os.path.join(PATH_TO_TEST_FILES, "test_audio_1_response.txt")

    with open(response_path, "wb") as f:
        f.write(response_file_content)

    assert os.path.getsize(response_path) > 0, "The response file is empty"
    assert "text/plain" in response.headers["content-type"], "The response file is not a .txt file with the correct charset"

    os.remove(response_path)