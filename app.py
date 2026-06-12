from pathlib import Path
import base64
import mimetypes

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).parent


def file_to_data_url(path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(path.name)

    if mime_type is None:
        if path.suffix.lower() == ".png":
            mime_type = "image/png"
        elif path.suffix.lower() in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        elif path.suffix.lower() == ".webp":
            mime_type = "image/webp"
        else:
            mime_type = "application/octet-stream"

    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def read_text_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def replace_local_images(content: str) -> str:
    image_folders = ["assets", "cards", "images"]
    image_extensions = [".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"]

    for folder_name in image_folders:
        folder = BASE_DIR / folder_name

        if not folder.exists():
            continue

        for image_path in folder.rglob("*"):
            if image_path.suffix.lower() not in image_extensions:
                continue

            relative_path = image_path.relative_to(BASE_DIR).as_posix()
            data_url = file_to_data_url(image_path)

            content = content.replace(relative_path, data_url)
            content = content.replace("./" + relative_path, data_url)

    return content


st.set_page_config(
    page_title="白猫タロット",
    page_icon="🐾",
    layout="wide",
)


html = read_text_file(BASE_DIR / "index.html")
css = read_text_file(BASE_DIR / "style.css")
js = read_text_file(BASE_DIR / "script.js")

page = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
{css}
</style>
</head>
<body>
{html}
<script>
{js}
</script>
</body>
</html>
"""

page = replace_local_images(page)

components.html(page, height=3200, scrolling=True)
