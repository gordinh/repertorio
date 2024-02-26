from pathlib import Path

import streamlit as st

from PIL import Image

# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() 
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Lucas_Morais_-_Software_Engineer.pdf"
profile_pic = current_dir / "assets" / "lucas_morais_software engineer.jpeg"
recommendation_letter = current_dir / "assets" / "recommendation_letter.pdf"