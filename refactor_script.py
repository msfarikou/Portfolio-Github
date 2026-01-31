import re

def refactor_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find style blocks
    # Looking for <style type="text/css">...</style> and extracting content inside <!-- --> if present
    style_pattern = re.compile(r'<style type="text/css">\s*(?:<!--)?(.*?)(?:-->)?\s*</style>', re.DOTALL)
    styles = style_pattern.findall(content)

    # Regex to find div pages
    # <div id="pageX-div" ...>...</div>
    # The div usually ends before </body>
    div_pattern = re.compile(r'(<div id="page\d+-div".*?</div>)', re.DOTALL)
    divs = div_pattern.findall(content)
    
    # Construct new HTML
    new_html = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
<title>Portfolio - MAMADOU SOUAHIBOU Farikou</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<style type="text/css">
<!--
	p {margin: 0; padding: 0;}
"""
    
    # Add all unique styles (avoiding p {margin: 0; padding: 0;} duplication if possible, but simplicity is key)
    # The original file has p {margin: 0; padding: 0;} in every block.
    # We will just append all style bodies.
    for style in styles:
        # Clean up commonly repeated rule if we want, but browser handles it fine.
        new_html += style + "\n"
        
    new_html += """-->
</style>
</head>
<body bgcolor="#A0A0A0" vlink="blue" link="blue">
"""

    for div in divs:
         new_html += div + "\n"

    new_html += """</body>
</html>"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    refactor_html('index.html')
