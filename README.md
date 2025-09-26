# 📊 Projeto - Consulta de Dados Econômicos e Integração com API (IBGE, BCB e Firebase)

Este projeto contém scripts em Python que realizam consultas a APIs públicas do **IBGE** e do **Banco Central do Brasil (BCB)**, além de operações CRUD em um banco de dados **Firebase Realtime Database**.

---

## 🚀 Tecnologias
- Python 3
- Biblioteca `requests`
- Biblioteca `json`
- Firebase Realtime Database

---

## 📂 Documentação dos Arquivos

### **APIs Econômicas**
- **`IBGE.py`** → Consulta o **IRSM (Índice de Reajuste do Salário Mínimo)** de junho/1994 usando a API do IBGE.  
- **`BANCO.py`** → Consulta a API do **Banco Central (Olinda/BCB)** para obter informações sobre dinheiro em circulação no Brasil.  

---

### **APIs Firebase (CRUD)**
- **`POST.py`** → Cria uma nova informação no banco (método **POST**).  
- **`PATCH.py`** → Atualiza uma informação existente no banco (método **PATCH**).  
- **`GET.py`** → Recupera todas as informações do banco (método **GET**).  
- **`DELETE.py`** → Remove uma informação específica do banco (método **DELETE**).  

---

## 📌 Observação
Cada arquivo possui **docstrings internas ou comentários** que explicam melhor o fluxo e as variáveis.
