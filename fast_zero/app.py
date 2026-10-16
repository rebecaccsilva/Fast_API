from fastapi import FastAPI

app= FastAPI()

@app.get('/batatinha')
def read_root():
    print('Olar mundis')
    return 'Batatinhas fritas voadoras'
    