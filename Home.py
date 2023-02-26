import streamlit as st

st.set_page_config(
    page_title="Finance-AI-App",
    page_icon="📈",
)

st.title("Finance AI")
st.sidebar.success("Successfully Loaded")

st.write(
    """
    In this app we have calculators for automating some of the financial challenges, You can explore the calculators
    on the sidebar.
    """
)

st.write(
    """
 Our finance calculator app is the perfect tool for anyone looking to make complex financial calculations with ease. With a simple and intuitive interface, our app is accessible to everyone, regardless of their level of financial knowledge.

Our app offers a wide range of calculators, including those for mortgage payments, loan payments, savings goals, and investment returns. Each calculator is easy to use and provides detailed information, allowing you to make informed decisions about your finances.   """
)



# Footer
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Twitter: [@william-mburu](https://twitter.com/WilliamCinemat)**', icon="👋")
with c2:
    st.info('**GitHub: [@SirWilliam254](https://github.com/Sirwilliam254)**', icon="💻")
with c3:
    st.info('**LinkedIn: [William Mburu](https://linkedin/in/william-mburu)**', icon="🌍")
