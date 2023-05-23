# flask-mapudungun
Diccionario Web en mapudungun
Contenidos basados en https://github.com/aldoberrios/Diccionario_Mapudungun

## Import export MongoDB

```
mongoimport --uri 'mongodb+srv://<usuario>:<senha>@<id>mongodb.net/mapuche_dic?retryWrites=true&w=majority' --type=csv --fields="id","mapudungun","raiz","gramatica","castellano","ejemplo","imagen","source" diccMAP_20230129_V01.csv

mongoexport --uri='mongodb+srv://<usuario>:<senha>@<id>mongodb.net/mapuche_dic'  --collection=diccMAP_20230129_V01  --out=diccMAP_20230129_V01.json
```
