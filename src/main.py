from fastapi import FastAPI
from src.models import Notification
from src.rules_engine import apply_rules
from src.decision_engine import decide

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notifications/evaluate")
def evaluate(notification: Notification):
    score = apply_rules(notification)
    decision = decide(score)

    return {
        "decision": decision,
        "reason": "Rule-based evaluation",
        "score": score
    }