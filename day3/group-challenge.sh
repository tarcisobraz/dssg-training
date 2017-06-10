#!/bin/bash

cat 2016.csv | grep USW00094846 | sed s/PRCP/RAIN/ | grep RAIN > ohare-rain-data.csv
