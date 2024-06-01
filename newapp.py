import streamlit as st
import pandas as pd
st.write("<h2 style='text-align: center;color: yellow;font-size:65px;'>SURAJ</h2>", unsafe_allow_html=True)

st.title("EAPCET College Recommender")
st.write("""Welcome to EAPCET college finder. We are here to help you to find the best colleges for BTECH in Telangana.

           NOTE: This tool provides only a basic understanding of
           allotments in Colleges.
           """)

st.write("These are the Districts with codes  Below..👇")
st.write("__"*30)

data = pd.read_excel(r"C:\Users\mahes\Downloads\TSEAMCET2022firstphase.xlsx")

def code():
    dist=["Hyderabad","Medchal","Ranga Reddy","Kothagudem","Suryapeta","Warangal","Khammam","Medak","Sangareddy","Kamareddy","NIzamadad","Karimnagar","Siddipet","Jagtial","Peddapally","Rajanna Sircilla","Wanaparthy","Mahabubnagar","Hanmakonda","Nalgonda","Yadadri bhuvanagiri"]
    codes=data["DIST"].unique()
    for i in range(len(dist)):
        st.write(f"{dist[i]}--{codes[i]}")
    st.write("--"*30)
code()
data.drop(["INST CODE", "PLACE", "BRANCH NAME", "COED", "TYPE", "YEAR OF ESTB", "TUITION FEE", "AFFILIATED"], axis=1,
          inplace=True)
data.columns = data.columns.str.lower()
print(data.columns)
st.write("Enter the required details to get the list of colleges.")
def search(rank,mycaste, branch, dist):
    st.write("*" * 30)
    c = 0
    lst = []
    lst2 = []
    branch = branch.upper()
    dist = dist.upper()
    d = data["dist"]
    b = data["branch"]
    inst = data["institute name"]

    for i in range(len(data["branch"])):
        if b[i] in branch:
            lst.append(i)
        if d[i] in dist:
            lst2.append(i)

    for i in range(len(data[mycaste])):
        if data[mycaste][i] >= int(rank)-1300:
            if i in lst and i in lst2:
                st.write(f"{inst[i]}, ({d[i]}) -- {b[i]}")
                c = 1

    if c == 0:
        st.write("No colleges available for the specified criteria")



rank = st.text_input("Enter your rank:")
caste = st.selectbox("Select your caste Category:", ["bc_a", "bc_b","bc_c","bc_d","bc_e","oc","ews"])
gen = st.selectbox("Select Gender:", ["Male", "Female"])
#st.write(f"You selected: {option}")
branch = st.text_input("Enter Wanted Branches:")

d = st.text_input("Enter DISTIRCT codes that you want to study:")
st.write("Suggest: you can give multipul Branches and District codes")
if gen=="Male":
    gen="boys"
else:
    gen="girls"
mycaste=caste+" "+gen
search(rank, mycaste, branch, d)

st.write("__"*30)
st.write("__"*30)

st.write("""The above provided colleges list is not final..
             This tool is developed only for basic understanding of allotments in colleges,,,""")
st.write("@All Rights Recived  ________________                 #SURAJ tech solutions")
