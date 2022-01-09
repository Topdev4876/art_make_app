import os,glob

folder_path = './Json'
for filename in glob.glob(os.path.join(folder_path, '*.json')):
  with open(filename, 'r') as f:
    text = f.read()
    text = text.replace('QmVkRQqYsuEBxweSPzXiD4WuVNniPpEY5jiEQwpD1ogU4a', 'QmUKJeCsZmzrFZHJFvtsXXkDadNBPQmpGLrCm8QipMrBEt')
  with open(filename, 'w') as f:
      f.write(text)
