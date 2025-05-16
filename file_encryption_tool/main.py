import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

class EncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption/Decryption Tool")
        self.root.geometry("400x300")

        self.key = None
        self.fernet = None

        tk.Label(self.root, text="File Encryption/Decryption Tool", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Generate Key", command=self.generate_key).pack(pady=5)
        tk.Button(self.root, text="Load Key", command=self.load_key).pack(pady=5)
        tk.Button(self.root, text="Encrypt File", command=self.encrypt_file).pack(pady=5)
        tk.Button(self.root, text="Decrypt File", command=self.decrypt_file).pack(pady=5)

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        with open("key.key", "wb") as key_file:
            key_file.write(self.key)
        messagebox.showinfo("Success", "Key generated and saved as key.key")

    def load_key(self):
        key_path = filedialog.askopenfilename(filetypes=[("Key files", "*.key")])
        if key_path:
            try:
                with open(key_path, "rb") as key_file:
                    self.key = key_file.read()
                self.fernet = Fernet(self.key)
                messagebox.showinfo("Success", "Key loaded successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load key: {str(e)}")

    def encrypt_file(self):
        if not self.fernet:
            messagebox.showerror("Error", "Please generate or load a key first")
            return
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"), ("All files", "*.*")])
        if file_path:
            try:
                # Check if file is readable
                with open(file_path, "rb") as file:
                    data = file.read()
                encrypted = self.fernet.encrypt(data)
                output_path = f"{file_path}.encrypted"
                with open(output_path, "wb") as file:
                    file.write(encrypted)
                messagebox.showinfo("Success", f"File encrypted as {output_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_file(self):
        if not self.fernet:
            messagebox.showerror("Error", "Please generate or load a key first")
            return
        file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.encrypted")])
        if file_path:
            try:
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()
                decrypted = self.fernet.decrypt(encrypted_data)
                # Remove '.encrypted' and add '.decrypted' while preserving original extension
                base_path = file_path.replace(".encrypted", "")
                output_path = f"{base_path}.decrypted"
                with open(output_path, "wb") as file:
                    file.write(decrypted)
                messagebox.showinfo("Success", f"File decrypted as {output_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionTool(root)
    root.mainloop()