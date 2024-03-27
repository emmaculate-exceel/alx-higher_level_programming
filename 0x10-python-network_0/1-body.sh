#!/bin/bash
#script that sends a GET request using curl
curl -s "$1" | grep -q "Route 2"
