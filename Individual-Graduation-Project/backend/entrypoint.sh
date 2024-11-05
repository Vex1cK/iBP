#!/bin/bash

A2T_MODEL_PATH="/app/ai_models/audio2text/whisper-large-v3"
CHECKSUM_FILE='/app/checksums.txt'
SKIP_CHECKSUMS=false

# Функция для загрузки модели
download_model_a2t() {
    echo "Подгружаем файлы модели A2T..."
    mkdir -p "$A2T_MODEL_PATH"
    huggingface-cli download openai/whisper-large-v3 --local-dir "$A2T_MODEL_PATH"
    echo "Модель A2T полностью загружена."
}

download_all_models() {
    download_model_a2t
}

verify_checksums() {
    cd /app
    echo "Проверка целостности файлов..."
    sha256sum -c "$CHECKSUM_FILE"
}

if [ ! -d "$A2T_MODEL_PATH" ] || [ -z "$(ls -A "$A2T_MODEL_PATH")" ]; then
    download_model_a2t
elif [ "$SKIP_CHECKSUMS" = false ] && ! verify_checksums; then
    echo "Целостность файлов нарушена. Подгружаем файлы..."
    download_all_models
else
    echo "Все файлы найдены и целостность файлов подтверждена."
fi

if [ "$1" = "test" ]; then
    cd /app
    pytest tests/ --disable-warnings
else
    cd /app/src
    uvicorn main:app --host 0.0.0.0 --port 8000
fi
