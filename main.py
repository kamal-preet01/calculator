import sqlite3
import streamlit as st


def create_database():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='customers'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE customers
                     (date text, party text, jobname text ,ply text, quantity text, sheetsize text, QLTY text,
                      GSM text, DRate text, dup text, rollsize text, rollGSM text,rollsize2 text, rollGSM2 text, rollsize3 text, rollGSM3 text,rollGSM_output text, 
                      rollGSM_output2 text ,rollGSM_output3 text,roll_a text ,roll_a2 text,roll_a3 text,lamksize text, lami text,lami_rate, col text, col1 text,col_rate text, nali text, 
                       Spast text, CandP text,total text, lab text, lab_cost text,
                      final_total text,div text,Rate text,Actual_rate text )''')
        conn.commit()
    conn.close()


def add_customer(date, party, jobname, ply, quantity, sheetsize, QLTY, GSM, DRate, dup,  rollsize, rollGSM,rollsize2, rollGSM2,rollsize3, rollGSM3,rollGSM_output,rollGSM_output2 ,rollGSM_output3, roll_a,roll_a2,roll_a3, lamksize, lami,lami_rate,col, col1,col_rate, nali, Spast, CandP,total, lab, lab_cost,final_total,div,Rate,Actual_rate ):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(date, party, jobname, ply, quantity, sheetsize, QLTY, GSM, DRate, dup,  rollsize, rollGSM,rollsize2, rollGSM2,rollsize3, rollGSM3,rollGSM_output,rollGSM_output2 ,rollGSM_output3, roll_a,roll_a2,roll_a3, lamksize, lami,lami_rate,col, col1,col_rate, nali, Spast, CandP,total, lab, lab_cost,final_total,div,Rate,Actual_rate) )
    conn.commit()
    conn.close()


def view_customers():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()
    return customers


def delete_customer(party):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE party=?", (party,))
    conn.commit()
    conn.close()




def main():
    create_database()

    date = st.date_input("")
    st.divider()


    party = st.text_input("Party", "")
    st.divider()

    jobname = st.text_input("Job Name", "")
    st.divider()

    ply = st.selectbox('PLY', (3, 5, 7))
    st.divider()

    quantity = st.text_input("Quantity", "")
    st.divider()

    sheetsize = st.text_input("sheet size", "")
    st.divider()

    QLTY = st.text_input("QLTY", "")
    st.divider()

    GSM = st.text_input("GSM", "")
    st.divider()

    DRate = st.text_input("D.Rate", "")


    if sheetsize and GSM and DRate:
        sheet_size_a = sheetsize.split("/")
        dup = round((float(sheet_size_a[0]) * float(sheet_size_a[1]) * float(GSM)) / 1550 * float(DRate) / 1000, 2)

        st.write("dup- ",dup)

    st.divider()

    rollsize2 = '_'
    rollGSM2 = '_'
    rollsize3 = '_'
    rollGSM3 = '_'
    roll_a2 = '_'
    roll_a3 = '_'
    rollGSM_output2 = '_'
    rollGSM_output3 = '_'
    lami_rate = '_'




    if ply == 3:
        rollsize = st.text_input("Roll size", "")
        st.divider()

        rollGSM = st.text_input("Roll GSM", "")
        if rollGSM:
            rollGSM_split = rollGSM.split("/")
            rollGSM_output = round(float(rollGSM_split[0]) + (float(rollGSM_split[1]) + 6.5) * 1.5)

            st.write("Roll GSM- ", rollGSM_output)
        st.divider()

        roll_a = st.text_input("Roll@", "")
        st.divider()


    if ply == 5:
        rollsize = st.text_input("Roll size", "")
        st.divider()

        rollGSM = st.text_input("Roll GSM", "")
        if rollGSM:
            rollGSM_split = rollGSM.split("/")
            rollGSM_output = round(float(rollGSM_split[0]) + (float(rollGSM_split[1]) + 6.5) * 1.5)
            st.write("Roll GSM - ", rollGSM_output)
        st.divider()

        rollsize2 = st.text_input("Roll size 2", "")
        st.divider()
        if rollsize2:
            roll_size_split2 = rollsize2.split("/")

        rollGSM2 = st.text_input("Roll GSM 2", "")
        if rollGSM2:
            rollGSM_split2 = rollGSM2.split("/")
            rollGSM_output2 = round(float(rollGSM_split2[0]) + (float(rollGSM_split2[1]) + 6.5) * 1.5)

            st.write("Roll GSM 2- ", rollGSM_output2)
        else:
            rollGSM_output2 = 9.75


        st.divider()

        roll_a = st.text_input("Roll@ ", "")
        st.divider()

        roll_a2 = st.text_input("Roll@ 2", "")
        st.divider()






    if ply == 7:
        rollsize = st.text_input("Roll size", "")
        st.divider()

        rollGSM = st.text_input("Roll GSM", "")
        if rollGSM:
            rollGSM_split = rollGSM.split("/")
            rollGSM_output = round(float(rollGSM_split[0]) + (float(rollGSM_split[1]) + 6.5) * 1.5)

            st.write("Roll GSM- ", rollGSM_output)
        st.divider()

        rollsize2 = st.text_input("Roll size 2", "")
        st.divider()
        if rollsize2:
            roll_size_split2 = rollsize2.split("/")


        rollGSM2 = st.text_input("Roll GSM 2", "")
        if rollGSM2:
            rollGSM_split2 = rollGSM2.split("/")
            rollGSM_output2 = round(float(rollGSM_split2[0]) + (float(rollGSM_split2[1]) + 6.5) * 1.5)

            st.write("Roll GSM 2- ", rollGSM_output2)
        else:
            rollGSM_output2 = 9.75

        st.divider()

        rollsize3 = st.text_input("Roll size 3", "")
        st.divider()
        if rollsize3:
            roll_size_split3 = rollsize3.split("/")

        rollGSM3 = st.text_input("Roll GSM 3", "")
        if rollGSM3:
            rollGSM_split3 = rollGSM3.split("/")
            rollGSM_output3 = round(float(rollGSM_split3[0]) + (float(rollGSM_split3[1]) + 6.5) * 1.5)

            st.write("Roll GSM 3- ", rollGSM_output3)
        else:
            rollGSM_output3 = 9.75

        st.divider()

        roll_a = st.text_input("Roll@", "")
        st.divider()

        roll_a2 = st.text_input("Roll@ 2", "")
        st.divider()

        roll_a3 = st.text_input("Roll@ 3", "")
        st.divider()

    roll_size_split = rollsize.split("/")

    if ply == 7:
        if rollsize3 and rollGSM3 and roll_a3:
            nali = round(float(roll_size_split[0]) * float(roll_size_split[1]) * float(rollGSM_output) / 1550 * float(roll_a) / 1000, 2) + \
                   (round(float(roll_size_split2[0]) * float(roll_size_split2[1]) * float(rollGSM_output2) / 1550 * float(roll_a2) / 1000, 2)) + \
                   (round(float(roll_size_split3[0]) * float(roll_size_split3[1]) * float(rollGSM_output3) / 1550 * float(roll_a3) / 1000, 2))

            st.write("nali- ", nali)
            st.divider()

    elif ply == 5:
        if rollsize2 and rollGSM2 and roll_a2:
             nali = round(float(roll_size_split[0]) * float(roll_size_split[1]) * float(rollGSM_output) / 1550 * float(roll_a) / 1000, 2) + (round(float(roll_size_split2[0]) * float(roll_size_split2[1]) * float(rollGSM_output2) / 1550 * float(roll_a2) / 1000, 2))

             st.write("nali- ", nali)
             st.divider()


    elif ply == 3:
        if rollsize and rollGSM and roll_a:
            nali = round(float(roll_size_split[0]) * float(roll_size_split[1]) * float(rollGSM_output) / 1550 * float(roll_a) / 1000, 2)

            st.write("nali- ", nali)
            st.divider()



    lamksize = st.text_input("Lamk size", "")
    st.divider()

    lami = st.text_input("Lami@", "")
    if lamksize and lami :
        lamksize_split = lamksize.split("/")
        lami_rate =round(float(lamksize_split[0]) * float(lamksize_split[1]) / float(lami) / 100, 2)
    elif lamksize == "" and lami:
        lami_rate = 0
    elif lamksize == "" and lami == "":
        lami_rate = 0


        st.write("lami rate- ",lami_rate)
    st.divider()


    col = st.text_input("Col", "")

    st.divider()

    col1 = st.text_input("Col@", "")

    if col1:
        if col == "":
            col_rate = 0
            st.write("print(col rate)-",col_rate)
        else:
            col_rate = round((float(col1) / 1000) * float(col), 2)

            st.write("print(col rate)- ",col_rate)
    elif col == "" and col1 == "":
        col_rate = 0
        st.write("print(col rate)- ", col_rate)

    st.divider()



    Spast = st.text_input("S Past", "")

    st.divider()
    CandP = st.text_input("C&P", "")


    if CandP:
        if Spast == "":
            total = round(float(dup) + float(CandP) + float(nali) + float(col_rate) + float(lami_rate),2)
            st.write("total- ", total)
        else:
            total= round(float(dup) + float(Spast) + float(CandP) + float(nali) + float(col_rate) + float(lami_rate), 2)
            st.write("total- ",total)
    st.divider()

    lab = st.text_input("Labour(%)","")

    if CandP and lab:
        lab_cost = round(float(total) * float(lab) / 100, 2)
    if lab:
        final_total = round(float(total) + float(lab_cost) , 2)

        st.write("total-",final_total)
    st.divider()

    div=st.text_input("Div","")
    if div:
        Rate=final_total / float(div)

        st.write("Rate-",Rate)

    st.divider()

    Actual_rate=st.text_input("Actual Rate","")
    if Actual_rate:
        st.write("actual rate- ",Actual_rate)
        st.divider()




    if st.button("Submit"):
        add_customer(date, party, jobname, ply, quantity, sheetsize, QLTY, GSM, DRate,dup, rollsize, rollGSM,rollsize2, rollGSM2,rollsize3, rollGSM3,rollGSM_output,rollGSM_output2 ,rollGSM_output3, roll_a,roll_a2,roll_a3,lamksize, lami,lami_rate, col, col1,col_rate, nali, Spast, CandP,total, lab, lab_cost,final_total,div,Rate,Actual_rate )
        st.success("Data Saved")


    st.header("Customer Details")

    st.divider()
    if st.button("View"):
        customers = view_customers()
        st.header("Customers File")
        st.table(customers)
    st.divider()

    if st.button("Delete"):
        delete_customer(party)
    st.divider()


if __name__ == '__main__':
    main()

