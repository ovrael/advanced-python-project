#############################
#                           #
#    Jacek Jendrzejewski    #
#     Maciej Baranowski     #
#           2023            #
#                           #
#############################

# Imports

# imports for fastApi
# import app.Helpers.className as className

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Advanced Programming in Python project"