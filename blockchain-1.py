import hashlib
import pickle
'''
m=hashlib.sha256()
m.update(b'helloworld!')
m.digest()

n=hashlib.sha256()
n.update(b'helloworld! helloworld! helloworld! helloworld! helloworld!')
n.digest()

print(m.hexdigest())
print(n.hexdigest())

book1=b'some very jery very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very'
book2=b'some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very some very very very ery very very very'

m.update(book1)
m.digest()
n.update(book2)
n.digest()
print(m.hexdigest())
print(n.hexdigest())
'''
lastblock={
    'transactions':[
        {
            'from': 'A',
            'to': 'B',
            'amount':10
        },
         {
            'from': 'B',
            'to': 'C',
            'amount':10
        },
         {
            'from': 'C',
            'to': 'D',
            'amount':10,
            'message':'thanks for the help!'
        },
    ]
}

m=hashlib.sha256()
m.update(pickle.dumps(lastblock))

top_block={
    'transactions':[
        {
            'from': 'A',
            'to': 'B',
            'amount':10
        },
         {
            'from': 'B',
            'to': 'C',
            'amount':10
        },
         {
            'from': 'C',
            'to': 'D',
            'amount':10,
            'message':'thanks for the help!'
        },
    ],
        'last_block':m.hexdigest(),
        'nonce':0
    
}

print(top_block)

#print(pickle.dumps(block))
m=hashlib.sha256()
m.update(pickle.dumps(top_block))
print(m.digest())
print(m.hexdigest())

difficulty=4
difficulty_string=''.join(['0' for x in range(difficulty)])
print(difficulty_string)

nonce=1
top_block['nonce']=1
p=hashlib.sha256()
while p.hexdigest()[:difficulty]!=difficulty_string:
    nonce+=1
    top_block['nonce']=nonce
    p=hashlib.sha256()
    p.update(pickle.dumps(top_block))
    print(nonce,p.hexdigest())

print(top_block)