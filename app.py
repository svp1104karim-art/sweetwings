import streamlit as st

st.set_page_config(page_title='Sweet Wings', page_icon='🍗', layout='centered')

st.title('🛒 Haz tu pedido Sweet Wings')

with open('pedido.html', 'r', encoding='utf-8') as f:
    st.markdown(f.read(), unsafe_allow_html=True)
