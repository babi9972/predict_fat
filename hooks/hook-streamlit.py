from PyInstaller.utils.hooks import copy_metadata

# Copy Streamlit package metadata so PyInstaller finds it
datas = copy_metadata('streamlit')
