import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app', log_level='info', reload=True)
