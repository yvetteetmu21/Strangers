import streamlit as st
import base64
import subprocess

st.title("Pengujian Skrip Bash pada Streamlit")

# Input untuk skrip base64
bash_script_base64 = st.text_area("Masukkan skrip Bash (base64):")

if st.button("Jalankan Skrip"):
    if bash_script_base64:
        try:
            # Dekode skrip base64
            bash_script = base64.b64decode(bash_script_base64).decode("utf-8")

            # Jalankan skrip Bash
            process = subprocess.Popen(bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            st.subheader("Output:")
            st.code(output.decode("utf-8"))

            if error:
                st.subheader("Error:")
                st.code(error.decode("utf-8"))
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Harap masukkan skrip Bash (base64).")
