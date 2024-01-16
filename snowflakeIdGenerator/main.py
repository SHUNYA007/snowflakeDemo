from fastapi import FastAPI,Depends
import concurrent.futures
from .uniqueIdGenerator import UniqueIdGenerator
app = FastAPI()

def call_generate_id (uniqueIdGenerate)
@app.get("/")
async def root(atomic: UniqueIdGenerator = Depends(UniqueIdGenerator)):
    result = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result_list = [executor.submit(atomic.generateid()) for _ in range(10)]
        for index, value in enumerate(concurrent.futures.as_completed(result_list)):
            result.update({index: value})  # Access result of completed future
    return result