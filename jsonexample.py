import json

a="""{
   "eBooks":[
      {
         "language":"Pascal",
         "edition":"third"
      },
      {
         "language":"Python",
         "edition":"four"
      },
      {
         "language":"SQL",
         "edition":"second"
      }
   ]
}"""

b=json.loads(a)

print(b['eBooks'][2])