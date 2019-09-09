# PortalApp

-------
<p align="center">
    <a href="#motivation">Motivation</a> &bull;
    <a href="#installation">Installation</a>
</p>
-------


## Motivation

This App was developed with the aim of improve my skills in Data Engineering, Front-End, Back-End using:
Python v3.7.3 (libs: os, glob, time)

The intention is to process Sales Data to create a Sales Analysis based using an archive with below layout:

Layout Archive:
001ç1234567891234çPedroç50000
001ç3245678865434çPauloç40000.99
002ç2345675434544345çJose da SilvaçRural
002ç2345675433444345çEduardo PereiraçRural
003ç10ç[1-10-100,2-30-2.50,3-40-3.10]çPedro
003ç08ç[1-34-10,2-33-1.50,3-40-0.10]çPaulo

## Installation

To execute this project, all you need to setup it properly is:

Using "Virtualenv"
```
# REQUIREMENTS:
# have installed Python (v3.7 prefered) on your LocalHost
# clone the repository (SalesAnalysis)

# Install Virtualenv
pip install virtualenv

# Inside of portalapp directory - Create the Virtual Enviroment
virtualenv -p 'python3' venv

# Inside of portalapp directory - Connect in the Virtual Environment
source venv/bin/activate

# Execute the commands to start
python SalesAnalysis.py

```
