import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version="10",
    company_name="IRRECO",
    file_description="Simple App",
    internal_name="Simple App",
    legal_copyright="© IRRECO. All rights reserved.",
    original_filename="ISSS.exe",
    product_name="Simple App",
    translations=[0, 1200]
)