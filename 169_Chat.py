# Importando as bibliotecas necessárias
import openai 
import streamlit as st
openai.api_key = "SUA_CHAVE_API_AQUI"
def chat_gpt(prompt): # Função para interagir com o modelo GPT-3.5
    try:
        response = openai.ChatCompletion.create( # Chamada para a API do OpenAI
            model="gpt-3.5-turbo",               # Modelo a ser utilizado
            messages=[
                {"role": "system", "content": "you are an english teacher and teach me how to write."},# Passando instruções para o modelo
                {"role": "user", "content": prompt} # Mensagem do usuário 
            ],
            max_tokens=150,  # maximo de tokens na resposta
            temperature=0.7, # temperatura para controlar a aleatoriedade da resposta
    )
        return response.choices[0].message['content'].strip() # Retorna o conteúdo da resposta do modelo
    except Exception as e:
        st.error(f"Erro ao se comunicar com a API: {e}")      # 
        return "Desculpe, não consegui processar sua solicitação." # Mensagem de erro caso ocorra algum problema


st.set_page_config(layout='centered') # Centraliza o layout da página
st.image("logo.png", width=200)       # Exibe uma imagem no topo da página
st.title("Chat com professor de Inglês Virtual") # Título da aplicação a ser exibido

user_input = st.text_input("Você: ", "")         # Campo de entrada de texto para o usuário

if user_input:                                   # Verifica se o usuário digitou algo
    
    prompt = "Aluno:{user_input} \nProfessor de Inglês:" # Prompt recebe a mensagem do usuário
    response = chat_gpt(prompt)                          # Chama a função para obter a resposta do modelo
    st.text_area("Professor:", value=response, height=200) # Exibe a resposta do modelo em um campo de texto
st.write("Digite sua pergunta ou mensagem acima e pressione Enter para conversar com o professor")
# st.write tem a função de exibir uma mensagem de instrução para o usuário