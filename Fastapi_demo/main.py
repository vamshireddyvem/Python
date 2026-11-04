from fastapi import FastAPI


app=FastAPI()

def greet():
    return print('Welcome to fastapi learning')