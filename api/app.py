from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def image():
    return """
    <html>
       <head>
         <title> My Sample </title>
       </head>
       <body>
       <h2> Hello world!! </h2>
       </body>
    </html>
    """


@app.get('/mail')
async def root():
    return {'message': 'Mail service will be added'}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)