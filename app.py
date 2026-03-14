import streamlit as st
import pandas as pd
# from agent.parser import parse_expense
from agent.txt_parser import parse_txt_with_ai
from utils.helpers import save_expenses

st.set_page_config(page_title="💰 Finance Assistant", layout="wide")
st.title("💰 Finance Assistant")

tab1, tab2 = st.tabs(["💬 Type Expense", "📁 Upload TXT File"])

# --- Tab 1: Natural language input ---
with tab1:
    user_input = st.text_input("Type your expense:", 
                                placeholder="e.g. Spent 250 on groceries today")
    
    if st.button("Parse", key="parse_single"):
        if user_input:
            with st.spinner("Parsing..."):
                result = parse_txt_with_ai(user_input)
                if result:
                    result = result[0]
                st.session_state['single_expense'] = [result]

    if 'single_expense' in st.session_state:
        st.write("### Review your expense:")
        edited_single = st.data_editor(
            pd.DataFrame(st.session_state['single_expense']),
            use_container_width=True
        )
        if st.button("✅ Save to Excel", key="save_single"):
            save_expenses(edited_single.to_dict(orient='records'))
            st.success("✅ Saved to Excel!")
            del st.session_state['single_expense']

# --- Tab 2: TXT file upload ---
with tab2:
    uploaded_file = st.file_uploader("Upload your expense txt file", type="txt")
    
    if uploaded_file:
        if st.button("Parse File", key="parse_file"):
            with st.spinner("AI is reading your file... (may take a few seconds)"):
                content = uploaded_file.read().decode("utf-8")
                parsed = parse_txt_with_ai(content)
                st.session_state['bulk_expenses'] = parsed

    if 'bulk_expenses' in st.session_state:
        st.write(f"### Found {len(st.session_state['bulk_expenses'])} expenses — edit if needed:")
        edited_df = st.data_editor(
            pd.DataFrame(st.session_state['bulk_expenses']),
            use_container_width=True
        )
        if st.button("✅ Save to Excel", key="save_bulk"):
            save_expenses(edited_df.to_dict(orient='records'))
            st.success(f"✅ Saved {len(edited_df)} expenses!")
            del st.session_state['bulk_expenses']