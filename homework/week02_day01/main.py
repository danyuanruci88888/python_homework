from fastapi import FastAPI
app = FastAPI()

@app.get("/") 
def read_root():
   return {"message":"Hello FastAPI"}

@app.get("/health")
def health_check():
   return  {"status":"ok"}

@app.get("/profile")
def profile():
   return {"name":"张三","target":"AI应用开发工程师"}