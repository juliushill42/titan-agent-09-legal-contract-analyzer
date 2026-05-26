#  2026 Julius Cameron Hill / TitanU AI LLC. All rights reserved. Patent pending JCH-2026-001.
from fastapi import FastAPI
from agent import LegalContractAnalyzerAgent

app = FastAPI(title="TitanU - Legal-Contract-Analyzer")
agent = LegalContractAnalyzerAgent()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
