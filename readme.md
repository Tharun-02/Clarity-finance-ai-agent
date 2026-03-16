# 💰 Finance AI Assistant

A **100% local** AI-powered personal finance assistant that parses expenses from natural language or text files, stores them in Excel, generates spending graphs, and answers questions about your spending — all without sending your data to any external service.

---

## Features

- 💬 **Type expenses naturally** — "Spent 250 on groceries today"
- 📁 **Upload a txt file** — bulk import expenses in a simple format
- ✏️ **Edit before saving** — review and correct AI-parsed data
- 📊 **Spending graphs** — pie chart, monthly breakdown, top 5 expenses
- 🤖 **Ask AI questions** — "How much did I spend on food this month?"
- 🔒 **100% local** — your data never leaves your machine

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Browser UI |
| Ollama + Llama 3.2 | Local AI model |
| pandas | Data processing |
| openpyxl | Excel read/write |
| matplotlib | Graphs |

---

## Project Structure

```
finance-ai-agent/
├── agent/
│   ├── __init__.py
│   └── txt_parser.py       # AI-powered expense parser
├── analytics/
│   ├── __init__.py
│   └── graphs.py           # Spending charts
├── data/
│   └── expenses.xlsx       # Auto-created on first save
├── images/
│   └── graphs/             # Saved graph images
├── llm/
│   ├── __init__.py
│   └── model_interface.py  # Q&A over spending data
├── tests/
│   ├── __init__.py
│   └── test_txt_parser.py  # Parser tests
├── utils/
│   └── helpers.py          # Excel save function
├── app.py                  # Streamlit app entry point
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Tharun-02/Clarity-finance-ai-agent.git
cd finance-ai-agent
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama and pull the model
Download Ollama from [ollama.com](https://ollama.com), then run:
```bash
ollama pull llama3.2
```

---

## How to Run

```bash
streamlit run app.py
```

This opens the app in your browser at `http://localhost:8501`

---

## Usage

### Tab 1 — Type an Expense
Type any natural language expense and click Parse:
```
Spent 250 on groceries today
Coffee 30
Paid 1200 for electricity bill
```

### Tab 2 — Upload a TXT File
Format your txt file like this:
```
Jan 1
coffee 30
groceries 1200
petrol 200

Jan 2
gym 900
whey protein 1500
```
Upload the file, review the parsed table, edit if needed, then save.

### Tab 3 — Graphs
View your spending broken down by:
- Category (pie chart)
- Month (bar chart)
- Top 5 expenses (horizontal bar)

### Tab 4 — Ask AI
Ask anything about your spending:
```
How much did I spend on food this month?
What was my biggest expense?
Show my total spending by category.
```

---

## Running Tests

```bash
python -m pytest tests/test_txt_parser.py -v
```

---

## Requirements

- Python 3.10+
- Ollama installed and running
- llama3.2 model pulled

---

## Future Upgrades

- [ ] Bank statement Excel upload
- [ ] Budget alerts
- [ ] Monthly financial report PDF
- [ ] Streamlit dashboard with filters
- [ ] SQLite database instead of Excel
- [ ] Receipt scanning with OCR