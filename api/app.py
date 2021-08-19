from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World!!'}

@app.get('/mail/')
async def mail():
    return 'Mail service will be added'

@app.get('/image/', response_class=HTMLResponse)
async def image():
    return """
    <html>
       <head>
         <title> My Sample </title>
       </head>
       <body>
       <h2> Hello </h2>
       </body>
    </html>
    """

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)