# Module 1 - Create a Blockchain

#Importing the libraries 
import datetime
import hashlib
import json
from flask import Flask, jsonfy

# Part 1 - Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        #genesis block (first block)
        self.create_block(proof = 1, previous_hash = "0")