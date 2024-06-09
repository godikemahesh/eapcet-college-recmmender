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
data = pd.read_csv("ts-eamcet-2022-final-rank converted.csv")

def code():
    dist=["Hyderabad","Medchal","Ranga Reddy","Kothagudem","Suryapeta","Warangal","Khammam","Medak","Sangareddy","Kamareddy","NIzamadad","Karimnagar","Siddipet","Jagtial","Peddapally","Rajanna Sircilla","Wanaparthy","Mahabubnagar","Hanmakonda","Nalgonda","Yadadri bhuvanagiri"]
    codes=data["DIST"].unique()
    for i in range(len(dist)):
        st.write(f"{dist[i]}--{codes[i]}")
    st.write("--"*30)
code()
data.drop(["INST CODE", "BRANCH NAME", "COED", "TYPE", "YEAR OF ESTB", "TUITION FEE", "AFFILIATED"], axis=1,inplace=True)
data1.drop(["INST CODE", "BRANCH NAME", "COED", "TYPE", "YEAR OF ESTB", "TUITION FEE", "AFFILIATED"], axis=1,inplace=True)
data1.columns = data1.columns.str.lower()
data.columns = data.columns.str.lower()
st.write("Enter the required details to get the list of colleges.")
def search1(name1,rank1,mycaste1,branch1,dist1):
    st.write("*"*30)
    st.write("<p style='text-align: left;color: yellow;'>ROUND- 2</p>", unsafe_allow_html=True)
    c = 0
    lst = []
    lst2 = []
    ind=[]
    branch1 = branch1.upper()
    dist1 = dist1.upper()
    p=data1["place"]
    d = data1["dist"]
    b = data1["branch"]
    inst = data1["institute name"]
    ind2=[]

    for i in range(len(data1["branch"])):
        if str(b[i]) in branch1:
            lst.append(i)
        if str(d[i]) in dist1:
            lst2.append(i)
    for i in range(len(data1[mycaste1])):
        if data1[mycaste1][i] >= rank1:
            ind.append(data1[mycaste1][i])
            ind=sorted(ind)

    for j in range(len(ind)):
        ind2.append(data1[data1[mycaste1]==ind[j]].index[0])

    for i in ind2:
        if dist1=="ALL":
            if i in lst:
                st.write(f"{inst[i]}, ({p[i]}) -- {b[i]}")
                c=1
        elif i in lst and i in lst2:
            st.write(f"{inst[i]}, ({p[i]}) -- {b[i]}")
            c = 1

    if c == 0:
        st.write("No colleges available for the specified criteria")


def search(name,rank,mycaste, branch, dist):
    st.write("*" * 30)
    st.write(f"Name: {name.upper()}")       
    st.write(f"Rank: {rank} ")
    st.write(f"Catageory: {mycaste} ")
    st.write(f"DIST: {dist.upper()}") 
    st.write("*"*30)       
    st.write("<p style='text-align: left;color: yellow;'>ROUND- 1</p>", unsafe_allow_html=True)
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
    if "HYD" in dist:
        dist=dist+" RR MDL"       
    for i in range(len(data["branch"])):
        if b[i] in branch:
            lst.append(i)
        if d[i] in dist:
            lst2.append(i)
    for i in range(len(data[mycaste])):
        if data[mycaste][i] >= rank:
            ind.append(data[mycaste][i])
            ind=sorted(ind)

    for j in range(len(ind)):
        ind2.append(data[data[mycaste]==ind[j]].index[0])
        
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
    search1(name,rank, mycaste, branch, d)

st.write("__"*30)
st.write("__"*30)

st.write("""The above provided colleges list is not final..
             This tool is developed only for basic understanding of allotments in colleges,,,""")
st.write("@All Rights Reserved  ________________                 #SURAJ tech solutions")
#st.write("<p style='text-align: right;color: yellow;'>@Mahesh_godike</p>", unsafe_allow_html=True)
