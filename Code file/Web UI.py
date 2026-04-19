import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Performance Analyzer")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    subjects = df.columns[1:6]

    df["Total"] = df[subjects].sum(axis=1)
    df["Percentage"] = df["Total"] / 5
    df["Status"] = df[subjects].apply(
        lambda x: "Pass" if all(x >= 35) else "Fail", axis=1
    )

    #  Top 5 with Rank
    top_5 = df.sort_values(by="Percentage", ascending=False).head(5).copy()
    top_5.insert(0, "Rank", range(1, len(top_5) + 1))
    
    st.subheader(" Top 5 Students")
    st.dataframe(top_5)
    
     # Bottom 5 with Rank
    bottom_5 = df.sort_values(by="Percentage", ascending=True).head(5).copy()
    bottom_5.insert(0, "Rank", range(1, len(bottom_5) + 1))

    st.subheader(" Bottom 5 Students")
    st.dataframe(bottom_5)

    pass_percent = (df["Status"] == "Pass").mean() * 100
    fail_percent = (df["Status"] == "Fail").mean() * 100

   

    st.subheader(" Statistics")
    st.write(f"Pass Percentage: {pass_percent:.2f}%")
    st.write(f"Fail Percentage: {fail_percent:.2f}%")






    st.bar_chart(df["Percentage"])
    
   
    
    counts = df["Status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
    st.pyplot(fig)
    csv = df.to_csv(index=False)

    




    # Create a clean summary table

    #  Subject-wise toppers table

    subjects = df.columns[1:6]
    
    topper_list = []
    
    for subject in subjects:
        max_marks = df[subject].max()
        topper_names = df[df[subject] == max_marks]["Name"].tolist()
    
        topper_list.append({
            "Subject": subject,
            "Topper(s)": ", ".join(topper_names),
            "Marks": max_marks
        })
    
    topper_df = pd.DataFrame(topper_list)
    
    st.subheader(" Subject-wise Toppers")
    st.dataframe(topper_df)

    
    
    
    failed_students = df[df["Status"] == "Fail"].copy()

    # Sort failed students (lowest percentage first)
    failed_students = failed_students.sort_values(by="Percentage", ascending=True)
    
    # Add Rank column
    failed_students.insert(0, "Sr. No.", range(1, len(failed_students) + 1))
    
    st.subheader(" Failed Students List")
    
    if not failed_students.empty:
        st.write(f"Total Failed Students: {len(failed_students)}")
        st.dataframe(failed_students)
    else:
        st.success(" No students failed!")


    
    
    st.download_button("Download Report", csv, "report.csv", "text/csv")
    st.sidebar.title("Tejas Sahane")
    st.sidebar.info("Upload file and analyze performance")
