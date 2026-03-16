import streamlit as st
import pandas as pd
from agent.txt_parser import parse_txt_with_ai
from utils.helpers import save_expenses
from analytics.graphs import category_pie_chart, monthly_bar_chart, top_expenses_chart
from llm.model_interface import ask_question

st.set_page_config(page_title="💰 Finance Assistant", layout="wide")
st.title("💰 Finance Assistant")

tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Type Expense", 
    "📁 Upload TXT", 
    "📊 Graphs", 
    "🤖 Ask AI"
])

# --- Tab 1: Natural language input ---
with tab1:
    user_input = st.text_input("Type your expense:",
                                placeholder="e.g. Spent 250 on groceries today")
    if st.button("Parse", key="parse_single"):
        if user_input:
            with st.spinner("AI is parsing..."):
                result = parse_txt_with_ai(user_input)
                if result:
                    st.session_state['single_expense'] = [result[0]]

    if 'single_expense' in st.session_state:
        st.write("### Review your expense:")
        edited_single = st.data_editor(
            pd.DataFrame(st.session_state['single_expense']),
            use_container_width=True
        )
        if st.button("✅ Save to Excel", key="save_single"):
            save_expenses(edited_single.to_dict(orient='records'))
            st.success("✅ Saved!")
            del st.session_state['single_expense']

# --- Tab 2: TXT file upload ---
with tab2:
    uploaded_file = st.file_uploader("Upload your expense txt file", type="txt")
    if uploaded_file:
        if st.button("Parse File", key="parse_file"):
            with st.spinner("AI is reading your file..."):
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

# --- Tab 3: Graphs ---
with tab3:
    st.write("### Spending Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = category_pie_chart()
        if fig1:
            st.pyplot(fig1)
        else:
            st.info("No data yet. Add some expenses first!")

    with col2:
        fig2 = monthly_bar_chart()
        if fig2:
            st.pyplot(fig2)
        else:
            st.info("No data yet. Add some expenses first!")

    fig3 = top_expenses_chart()
    if fig3:
        st.pyplot(fig3)

# --- Tab 4: Ask AI ---
with tab4:
    st.write("### Ask anything about your spending")
    
    # Show example questions
    st.caption("Examples: 'How much did I spend on food?' · 'What was my biggest expense?' · 'Total spending this month?'")
    
    question = st.text_input("Your question:", placeholder="How much did I spend on food?")
    
    if st.button("Ask", key="ask_ai"):
        if question:
            with st.spinner("AI is thinking..."):
                answer = ask_question(question)
                st.session_state['last_answer'] = answer

    if 'last_answer' in st.session_state:
        st.write("### Answer:")
        st.write(st.session_state['last_answer'])