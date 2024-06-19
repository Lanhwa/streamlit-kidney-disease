import streamlit as st

from web_funcsion import predict

def app(df, x, y):
    st.title("Halaman Prediksi")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input ('Input Blood Pressure')
    with col1:
        sg = st.text_input ('Input Specific Gravity')
    with col1:
        al = st.text_input ('Input Albumin')
    with col1:
        su = st.text_input ('Input Sugar')
    with col1:
        rbc = st.text_input ('Input Red Blood Cells')
    with col1:
        pc = st.text_input ('Input Pus Cell')
    with col1:
        pcc = st.text_input ('Input Pus Cell Clumps')
    with col1:
        ba = st.text_input ('Input Bacteria')
    with col2:
        bgr = st.text_input ('Input Blood Glucose Random')
    with col2:
        bu = st.text_input ('Input Blood Urea')
    with col2:
        sc = st.text_input ('Input Serum Creatinine')
    with col2:
        sod = st.text_input ('Input Sodium')
    with col2:
        pot = st.text_input ('Input Potassium')
    with col2:
        hemo = st.text_input ('Input Hemoglobin')
    with col2:
        pcv = st.text_input ('Input Packed Cell Volume')
    with col2:
        wc = st.text_input ('Input White Blood Cell Count')
    with col3:
        rc = st.text_input ('Input Red Blood Cell Count')
    with col3:
        htn = st.text_input ('Input Hypertension')
    with col3:
        dm = st.text_input ('Input Diabetes Mellitus')
    with col3:
        cad = st.text_input ('Input Coronary Artery Disease')
    with col3:
        appet = st.text_input ('Input Appetite')
    with col3:
        pe = st.text_input ('Input Pedal Edema')
    with col3:
        ane = st.text_input ('Input Anemia')

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    # tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Berhasil...")

        if (prediction == 1):
            st.warning("Pasien tersebut rentan terkena penyakit ginjal \n Segera lakukan pemeriksaan untuk penanganan lebih lajut")
        else:
            st.success("Pasien tersebut relatif aman dari penyakit ginjal \n Teruslah jaga kesehatan dan rutin berolahraga")

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")