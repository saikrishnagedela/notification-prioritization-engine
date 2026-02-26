# Notification Prioritization Engine

## Problem
Users receive too many notifications from multiple services.
This system decides whether a notification should be:

- NOW (send immediately)
- LATER (schedule)
- NEVER (suppress)

## Objective
Reduce alert fatigue while ensuring important notifications are delivered.

---

## Architecture Overview
The system processes incoming notification events using:

- Rule Engine
- AI Scoring Layer
- Duplicate Detection
- Fatigue Controller
- Decision Engine
- Audit Logging

---

## Decision Flow
1. Receive notification
2. Check duplicates
3. Apply configurable rules
4. AI priority scoring
5. Alert fatigue check
6. Final decision (Now/Later/Never)
7. Store explanation log

---

## APIs
- POST /notifications/evaluate
- GET /decision/{event_id}
- POST /rules/update
- GET /health

---

## Technologies
- Python
- FastAPI
- Rule-based + AI-assisted scoring

---

## AI Usage Disclosure
ChatGPT was used for architecture brainstorming and documentation drafting.
All final design decisions were manually reviewed and modified.

---

## Run Project

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
