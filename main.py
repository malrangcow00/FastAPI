from fastapi import FastAPI
from pandas import read_csv

app = FastAPI()

@app.get("/")
async def read_root():
    return "this page for test fastapi"

@app.get("/load-welfare-data")
async def load_welfare_data():
    file_path = "C:/Users/SSAFY/Desktop/dataset/복지서비스.csv"
    try:
        # CSV 파일을 읽어 DataFrame으로 변환
        df = read_csv(file_path)

        # NaN 값을 빈 문자열로 대체
        df.fillna("", inplace=True)

        # DataFrame을 JSON 형식의 문자열로 변환하여 반환

        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
