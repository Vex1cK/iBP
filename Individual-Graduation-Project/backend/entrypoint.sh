A2T_MODEL_PATH="/app/ai_models/audio2text/whisper-large-v3"
SUM_MODEL_PATH="/app/ai_models/text2text_summary/bert-large-uncased"
CHECKSUM_FILE="/app/checksums.txt"
SKIP_CHECKSUMS=false

download_model_a2t() {
    echo "Подгружаем файлы модели A2T..."
    mkdir -p "$A2T_MODEL_PATH"
    huggingface-cli download openai/whisper-large-v3 --local-dir "$A2T_MODEL_PATH"
    echo "Модель A2T полностью загружена."
}

download_model_sum() {
    echo "Подгружаем файлы модели SUM..."
    mkdir -p "$SUM_MODEL_PATH"
    huggingface-cli download bert-large-uncased --local-dir "$SUM_MODEL_PATH"
    echo "Модель SUM полностью загружена."
}

download_all_models() {
    download_model_a2t
    download_model_sum
}

verify_checksums() {
    cd /app
    echo "Проверка целостности файлов..."
    sha256sum -c "$CHECKSUM_FILE"
}

if [ ! -d "$A2T_MODEL_PATH" ] || [ -z "$(ls -A "$A2T_MODEL_PATH")" ]; then
    download_model_a2t
fi

if [ ! -d "$SUM_MODEL_PATH" ] || [ -z "$(ls -A "$SUM_MODEL_PATH")" ]; then
    download_model_sum
fi

if [ "$SKIP_CHECKSUMS" = false ] && ! verify_checksums; then
    echo "Целостность файлов нарушена. Подгружаем файлы..."
    download_all_models
elif [ "$SKIP_CHECKSUMS" = true ]; then
    echo "Пропускаем проверку целостности файлов."
else
    echo "Все файлы найдены и целостность файлов подтверждена."
fi

if [ "$1" = "test" ]; then
    cd /app
    pytest tests/ --disable-warnings --timeout=1800
elif [ "$1" = "lint" ]; then
    cd /app
    flake8 . --max-line-length=120 --ignore=W292,E402,E302,W293,W291,E712 --exclude=alembic,__init__.py,qt_app/src/tests/,qt_app/src/ui_module/ || exit 1
else
    cd /app/src
    uvicorn main:app --host 0.0.0.0 --port 8000
fi
