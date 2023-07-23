import streamlit as st 
from dotenv import load_dotenv




def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDfs", page_icon=":books:")
    
    st.header("Chat with multiple PDfs :books:")
    st.text_input("Ask a question about your documments:")
    

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and press click on 'Process'")
        st.button("Process")



if __name__ == '__main__':
    main()