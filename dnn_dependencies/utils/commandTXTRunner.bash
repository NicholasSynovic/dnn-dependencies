#!/bin/bash

NPY_DISABLE_CPU_FEATURES="AVX2,FMA3"

parallel --bar < commands.txt
