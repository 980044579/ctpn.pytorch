#!/bin/sh

PWD=$(cd -P -- "$(dirname -- "$0")" && pwd -P) # 这一行命令可以得到 run.sh 所在目录
ls -l $PWD

python ctpn_train.py --image-dir ${DATA_DIR} 
