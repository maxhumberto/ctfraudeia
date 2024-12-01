import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("upload de arquivo Dio - Desafio 1 - Azure - Fae Docs")
    uploaded_file = st.file_uploader("Escolha um aquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not Nome:
        fileName = uploaded_file.name

        blob_url: upload_blob(upload_file, fileName)
        if blob_url:
            st.write(f"Arquivo selecionado: {fileName}")
            credit_card_info = analize_credit_card(blob_url)
            show_imagem_and_validation(blob_url, credit_card_info)
        else:
            st.write("Nenhum arquivo selecionado {fileName} ")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Arquivo selecionado')
    st.write("imagem do cartao encontraada")
    st.write(credit_card_info)
    if credit_card_info and credit_card_info["card name"]:
        st.markdown(f"<h1 style='color: green;'> cartao valido</h1>", unsafe_allow_html=True)
        st.write(f"nome do titular: {credi_card_info['card_name']}")
        
    else:
        st.markdown(f"<h1 style='color: red;'> cartao invalido</h>", unsafe_allow_html=True)
        st.write("Este não é um cartao de credito valido")





 if _name_ == "_main_":
    configure_interface()
