import uvicorn
import os
import concurrent.futures
from dotenv import load_dotenv
from snowflakeIdGenerator import main

load_dotenv()

def run_uvicorn(port):
    uvicorn.run("snowflakeIdGenerator.main:app", host=os.getenv('HOST'), reload=False, port=port)



       

if __name__ == "__main__":
    ports = [int(os.getenv('PORT')), 8001]
    with concurrent.futures.ProcessPoolExecutor() as executer:
        executer.map(run_uvicorn,ports)