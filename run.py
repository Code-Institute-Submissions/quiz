import os
import json
from flask import Flask, render_template, request, redirect, url_for
from collections import deque
import quiz