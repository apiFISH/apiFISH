

#!/usr/bin/env bash
set -euo pipefail

# Build apiFISH documentation using uv.
# Run from anywhere: ./build_doc.sh

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

VENV_DIR="$ROOT_DIR/.venv-docs"
PYTHON_VERSION="3.11"
OUTPUT_DIR="$ROOT_DIR/docs/build/html"

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is not installed."
    echo "See https://docs.astral.sh/uv/"
    exit 1
fi

echo ">>> Preparing Python environment..."

if [[ ! -x "$VENV_DIR/bin/python" ]]; then
    uv venv --python "$PYTHON_VERSION" "$VENV_DIR"
fi

echo ">>> Installing documentation dependencies..."

uv pip install --python "$VENV_DIR/bin/python" \
    -r docs/requirements.txt

echo ">>> Installing apiFISH without runtime dependencies..."

uv pip install --python "$VENV_DIR/bin/python" \
    --no-deps -e .

echo ">>> Building documentation..."

"$VENV_DIR/bin/python" -m sphinx \
    -b html \
    docs/source \
    "$OUTPUT_DIR"

echo ""
echo ">>> Documentation built successfully!"
echo ">>> Output: $OUTPUT_DIR/index.html"
echo ""

# Open documentation only when explicitly requested.
if [[ "${1:-}" == "--open" ]]; then
    if command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$OUTPUT_DIR/index.html"
    else
        echo "Open $OUTPUT_DIR/index.html in your browser."
    fi
fi
