from distutils.core import setup

setup(
    name="efocus",
    packages=["efocus"],
    version="0.1.1",
    license="MIT",
    description="Simple command-line based debugger",
    author="Uri Shimon",
    author_email="uri.shimon5@gmail.com",
    url="https://github.com/shimonuri/cmdb",
    download_url="https://github.com/shimonuri/cmdb/archive/v0.1.1.zip",
    keywords=["DEBUGGER", "CMD", "LOGGING"],
    install_requires=["click",],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
