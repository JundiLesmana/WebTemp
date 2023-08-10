import streamlit as st
import easymodbus.modbusClient

#----------------------------mulai fungsi ---------------------------------
#fungsi baca plc
def bacaplc():
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.35', 502)
    modbusclient.connect()
    QW128 = modbusclient.read_inputregisters(1,1) #30001 suhu, humidity 30002
    modbusclient.close()
    
    QW128 = str(QW128)
    QW128 = QW128.replace("[","")
    QW128 = QW128.replace("]","")
    QW128 = float(QW128)/10    
    QW128s = "HUMIDITY : " + str(QW128)
    lblDataQW128.config(text=QW128s,
                    font=('arial', 28, 'bold'),
                    bg=bg,fg='blue') 
    root.after(500, bacaplc)

"""
#fungsi tulis plc
def tulisplcon():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,True)
    modbusclient.close()
def tulisplcoff():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,False)
    modbusclient.close()
"""
    
#----------------------------akhir fungsi ---------------------------------


#----header section-------
st.subheader("Selamat datang :wave:")
st.title ("Para pejuang masa depan")
st.write("kami akan membantu kamu agar tujuan kamu tercapai")
st.write ("[Lainnya >])(https://jundilesmana.blogspot.com)")

#-------interaksi-----------
with st.container():
        st.write("---")
        left_column, right_column = st.column(2)
        with left_column:
            st.header("Interaksi")
            st.write("##")
            st.write(
                """
               halo, Nama lengkap saya Jundulloh rizki ananda,teman dekat saya biasa memanggil Jundi Lesmana salam kenal untuk kalian semua 
            yang mengunjungi portofolio saya,saya lulusan SMK IT ISTANA MULIA 
               """
            )
        

st.write("""# Belajar Web dengan Python
         Ini adalah aplikasi web
          """)
#adding a button

if st.button('Siap Belajar ?'):

    st.write('Selamat Belajar') #displayed when the button is clicked
#else:
    #st.write('Have a great day') #displayed when the button is unclicked
    
if st.button('Q0.3 ON'):
    st.write(tulisplcon()) #
if st.button('Q0.3 OFF'):
    st.write(tulisplcoff()) #
