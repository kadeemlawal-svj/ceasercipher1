# Caesar Cipher

A small web app that encrypts and decrypts messages with a Caesar cipher.
Letters are shifted by the selected key; spaces, numbers, and punctuation are
left unchanged.

## Install

Open a terminal in this folder and create a virtual environment:

```text
python -m venv .venv
```

Activate it on Windows:

```text
.venv\Scripts\activate
```

On macOS or Linux, activate it with:

```text
source .venv/bin/activate
```

Install Flask:

```text
pip install -r requirements.txt
```

## Run

Start the server:

```text
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

Enter a message and a key from 1 to 25, then choose Encrypt or Decrypt.

## Example

With the message `Meet me at 8 PM!` and key `3`:

- Encrypted: `Phhw ph dw 8 SP!`
- Decrypted: `Meet me at 8 PM!`
