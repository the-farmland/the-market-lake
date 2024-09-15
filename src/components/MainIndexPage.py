# MainIndexPage.py
from src.components.MainPlusPlaceholderImageBase64BinaryData import plus_placeholder_svg  # Import the SVG content

main_index_html = f"""
<html style="background:#000000;">
    <body style="display:flex; justify-content: center; align-items: center; width: 100%; height:100%;">
        <div>Hello World</div>
        {plus_placeholder_svg}  <!-- Insert the SVG directly into the HTML -->
    </body>
</html>
"""
