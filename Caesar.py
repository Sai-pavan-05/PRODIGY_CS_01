import streamlit as st

# Caesar Cipher core function
def caesar_cipher(text, shift):
    """General Caesar Cipher with shift (positive for encryption, negative for decryption)."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Encrypt = forward shift
def encrypt_caesar(text, shift):
    return caesar_cipher(text, shift)

# Decrypt = backward shift
def decrypt_caesar(text, shift):
    return caesar_cipher(text, -shift)


# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Caesar Cipher Tool", page_icon="🔐", layout="centered")

st.title("🔐 Caesar Cipher Tool")

# Keep stateful "current message" inside session state
if "current_message" not in st.session_state:
    st.session_state.current_message = ""

# Input area
message = st.text_area("Enter your message:", st.session_state.current_message, height=150)

shift = st.slider("Select shift value", 1, 25, 3)

col1, col2 = st.columns(2)

with col1:
    if st.button("Encrypt"):
        encrypted = encrypt_caesar(message, shift)
        st.session_state.current_message = encrypted
        st.success("Message encrypted ✅")
        st.text_area("Encrypted Message:", encrypted, height=150)

with col2:
    if st.button("Decrypt"):
        decrypted = decrypt_caesar(message, shift)
        st.session_state.current_message = decrypted
        st.success("Message decrypted ✅")
        st.text_area("Decrypted Message:", decrypted, height=150)

st.caption("Tip: After encryption, the message box automatically updates, so you can decrypt immediately by clicking 'Decrypt'.")
