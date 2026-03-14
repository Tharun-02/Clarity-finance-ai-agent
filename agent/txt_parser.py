import ollama
import json

def parse_txt_with_ai(content: str):
    prompt = f"""
    Extract all expenses from the text below.
    Return ONLY a JSON array, no explanation.
    
    Each item must have:
    - date (Month date - Jan 1 format, guess year as 2026)
    - description
    - amount (number only)
    - category (guess from description, e.g. Food, Transport, Health)
    - payment_method (set as "Spending" if not mentioned)

    Text:
    {content}

    Return only valid JSON like this:
    [
      {{"date": "01-01-2026", "description": "coffee", "amount": 30, "category": "Food", "payment_method": "Spending"}}
    ]
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0, "num_predict": 2000} 
    )

    raw = response['message']['content']

     # ADD THIS to see what the AI actually returned
    print("=== RAW AI RESPONSE ===")
    print(raw)
    print("=== END ===")
    
    # Extract JSON safely
    start = raw.find('[')
    end = raw.rfind(']') + 1
    return json.loads(raw[start:end])