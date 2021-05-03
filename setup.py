setup(
    name="Engage-Auto-Download",
    version="1.0.0",
    description="Helps students sync recording files for Engage that are on Google Drive",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Themood/Engage-Recording-Auto-Download",
    author="Mahmood Gladney",
    author_email="mahmoodgladney@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["auto-download"],
    include_package_data=True,
    install_requires=[
        "pydrive", "adb_shell", "tkinter", "cefpython"
    ],
    entry_points={"gui_scripts": ["auto-download=autoDownload.ui:main"]}
)