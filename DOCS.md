Main link - ///

All requests are POST (JSON)

## ROUTE:

### /registration
**Input**:
```json
{
'data':
	 {
     'name': 't1e2st',
	 'password': 'test',
	 'contraindications': 'testing, tree ewfw ef wef we f we f'
	 }
 }
```
**Output**
```json
{
'status': 'success' or 'errore'
'message': 'User created' or 'User with this name already exist'
}
```
---
### /edit
**Input**:
```json
{
'data':
	 {
     'name': 't1e2st',
	 'password': 'test',
	 'contraindications': 'tree chocolate'
	 }
 }
```
**Output**
```json
{
'status': 'success' or 'errore'
'message': True or False
}
```
---
### /get
**Input**:
```json
{
'data':
	{
    'name': 't1e2st',
	'password': 'test'
	}
 }
```
**Output**
```json
{
'status': 'success' or 'errore'
'message': 'tree chocolate' or False
}
```

---
### /upload (Delays may occur during execution)
**Input**:
```json
{
'data':
    {
    'name': 'te2st',
    'password': 'test',
    'image': image_base64
    }
}
```
**Output**
```json
{
'status': 'success' or 'errore'
'message': TrueAnswer or 'No image data provided'
}
```
---

It's all.