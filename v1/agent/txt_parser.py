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
        options={"temperature": 0, "num_predict": 4000} 
    )

    raw = response['message']['content']

    start = raw.find('[')
    end = raw.rfind(']') + 1

    if start == -1:
        return []
    
    # If ] is missing, add it to close the array
    if end == 0:
        raw = raw + "]"
        end = len(raw)

    try:
        return json.loads(raw[start:end])
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error: {e}")
        return []

     # ADD THIS to see what the AI actually returned
    print("=== RAW AI RESPONSE ===")
    print(raw)
    print("=== END ===")
    
    # Extract JSON safely
    start = raw.find('[')
    end = raw.rfind(']') + 1
    return json.loads(raw[start:end])