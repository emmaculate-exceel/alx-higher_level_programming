#!/bin/bash
#script to displays the size of the body response
curl -s "$1" | wc -c
