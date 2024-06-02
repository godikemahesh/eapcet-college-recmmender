import streamlit as st
import pandas as pd
st.write("<h2 style='text-align: center;color: yellow;font-size:65px;'>SURAJ®</h2>", unsafe_allow_html=True)

st.title("EAPCET College Recommender")
st.write("""Welcome to EAPCET college Recommender. We are here to help you to find the best colleges for BTECH in Telangana.

           NOTE: This tool provides only a
           basic understanding of allotments
           in the Btech Intitutes.
           """)

st.write("Here the Districts with codes  Below..👇")
st.write("__"*30)

data = pd.read_csv("TSEAMCET2022firstphase.csv")

def code():
    dist=["Hyderabad","Medchal","Ranga Reddy","Kothagudem","Suryapeta","Warangal","Khammam","Medak","Sangareddy","Kamareddy","NIzamadad","Karimnagar","Siddipet","Jagtial","Peddapally","Rajanna Sircilla","Wanaparthy","Mahabubnagar","Hanmakonda","Nalgonda","Yadadri bhuvanagiri"]
    codes=data["DIST"].unique()
    for i in range(len(dist)):
        st.write(f"{dist[i]}--{codes[i]}")
    st.write("--"*30)
code()
data.drop(["INST CODE", "BRANCH NAME", "COED", "TYPE", "YEAR OF ESTB", "TUITION FEE", "AFFILIATED"], axis=1,
          inplace=True)
data.columns = data.columns.str.lower()
st.write("Enter the required details to get the list of colleges.")
def search(name,rank,mycaste, branch, dist):
    st.write("*" * 30)
    st.write(f"Name: {name.upper()}")       
    st.write(f"Rank: {rank} ")
    st.write(f"Catageory: {mycaste} ")
    st.write(f"DIST: {dist.upper()}")       
    c = 0
    lst = []
    lst2 = []
    ind=[]
    branch = branch.upper()
    dist = dist.upper()
    p=data["place"]
    d = data["dist"]
    b = data["branch"]
    inst = data["institute name"]
    ind2=[]
    cnt=1
    for i in range(len(data["branch"])):
        if b[i] in branch:
            lst.append(i)
        if d[i] in dist:
            lst2.append(i)
    for i in range(len(data[mycaste])):
        if data[mycaste][i] >= rank-1300:
            ind.append(data[mycaste][i])
            ind=sorted(ind)

    for j in range(len(ind)):
        ind2.append(data[data[mycaste]==ind[j]].index[0])
        print()
    for i in ind2:
        if dist=="ALL":
            if i in lst:
                st.write(f"{cnt}) {inst[i]}, ({p[i]}) -- {b[i]}")
                cnt=cnt+1       
                c=1
        elif i in lst and i in lst2:
            st.write(f"{cnt}) {inst[i]}, ({p[i]}) -- {b[i]}")
            cnt=cnt+1
            c = 1

    if c == 0:
        st.write("No colleges available for the specified criteria")


name=st.text_input("Enter your Name:")
rank = st.number_input("Enter your rank:")
caste = st.selectbox("Select your caste Category:", ["bc_a", "bc_b","bc_c","bc_d","bc_e","sc","st","oc","ews"])
gen = st.selectbox("Select Gender:", ["Male", "Female"])
#st.write(f"You selected: {option}")
branch = st.text_input("Enter Wanted Branches:")

d = st.text_input("Enter DISTIRCT codes that you want to study:")
st.write("Suggest: you can give multipul Branches and District codes")
if d=="":
    d="ALL"
if gen=="Male":
    gen="boys"
else:
    gen="girls"
mycaste=caste+" "+gen
btn=st.button("get colleges")
if btn:
    search(name,rank, mycaste, branch, d)

st.write("__"*30)
st.write("__"*30)

st.write("""The above provided colleges list is not final..
             This tool is developed only for basic understanding of allotments in colleges,,,""")
st.write("@All Rights Reserved  ________________                 #SURAJ tech solutions")
#st.write("<p style='text-align: right;color: yellow;'>@Mahesh_godike</p>", unsafe_allow_html=True)
