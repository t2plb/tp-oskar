from fastapi.testclient import TestClient
from main import *
from database import get_db

app = FastAPI(
    title="TP API FastAPI",
    description="Hello guys welcome.",
    version="1.0.0"
)

client = TestClient(app)

def test_not_found():
    response = client.get("/jaaj/")
    assert response.status_code == 404

def test_perf(benchmark):
    db = next(get_db()) 
    result = benchmark(lambda: get_customers(db))
    assert isinstance(result, list)