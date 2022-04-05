mkdir -p ~/.streamlit/

echo "[server]\nheadless = true\nport = $PORT\nenableCORS = false\n" > ~/.streamlit/config.toml
