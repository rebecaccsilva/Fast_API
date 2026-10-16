from fastapi import FastAPI

app = FastAPI()


@app.get('/batatinha')
def read_root():
    return {'message': 'Olar mundis!!'}
