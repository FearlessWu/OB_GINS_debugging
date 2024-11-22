#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    compile_mode = 'release'
    if len(sys.argv) > 1:
        compile_mode = sys.argv[1]

    os.system('rm -rf ./bin/')
    os.system('rm  -rf ./build/')
    os.system('mkdir ./build && mkdir ./bin')
    print('clean ./bin/ ./build/')
    if compile_mode == 'debug':
        os.system('cd ./build && cmake ../ -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_COMPILER=gcc-11 -DCMAKE_CXX_COMPILER=g++-11 && make -j16')
    else:
        os.system('cd ./build && cmake ../ -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=gcc-11 -DCMAKE_CXX_COMPILER=g++-11 && make -j16')