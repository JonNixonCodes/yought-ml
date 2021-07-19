#!/bin/sh
conda install -c -y conda-forge textblob
python -m textblob.download_corpora lite