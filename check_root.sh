#!/bin/bash

if [ "$EUID" -ne 0 ]
  then 
  exit 1
fi