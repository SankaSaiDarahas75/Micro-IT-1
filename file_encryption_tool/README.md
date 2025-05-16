File Encryption/Decryption Tool
A simple tool to encrypt and decrypt files using the cryptography library in Python. Supports .txt and .pdf files with a user-friendly GUI.
Setup
Install dependencies: pip install -r requirements.txt
Run the app: python main.py
Usage
Launch the Application:
Run python main.py to open the GUI.
You will see the main window with buttons to select files, generate/load keys, and encrypt/decrypt files.
Screenshot:
Generate or Load a Key:
Click "Generate Key" to create a new encryption key (saved as key.key).
Alternatively, click "Load Key" to select an existing key.key file.
Screenshot:
Select Files:
Click "Select Files" to choose one or more .txt or .pdf files for encryption/decryption.
The selected file names will appear below the button.
Screenshot:
Encrypt Files:
Click "Encrypt Files" to encrypt the selected files. Each file will be saved with a .encrypted extension.
A progress bar will show the encryption progress.
Screenshot:
Decrypt Files:
Select .encrypted files and click "Decrypt Files" to decrypt them. Decrypted files will have a .decrypted extension.
The progress bar will show the decryption progress.
Screenshot:
Clear State:
Click "Clear" to reset the selected files and progress bar.
Key Management
Storing the Key: The encryption key is saved as key.key in the project directory when you generate a new key. Store key.key securely, as it is required to decrypt files. Do not share it publicly or lose it, as files cannot be decrypted without the correct key.
Backup: Keep a backup of key.key in a secure location (e.g., an encrypted USB drive or password manager).
Loading Keys: Use the "Load Key" button to load a previously generated key.key file if needed.
Notes
Ensure the cryptography library is installed via requirements.txt.
Test the tool with sample files in the sample_files directory (data.pdf, test.txt).