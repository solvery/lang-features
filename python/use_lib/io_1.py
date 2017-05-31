# python3
import io

sf = io.StringIO()
sf.write('hello')
sf.write(' ')
sf.write('world')
print (sf.getvalue())

bf = io.BytesIO()
bf.write('中文'.encode('utf-8'))
print (bf.getvalue()) 
