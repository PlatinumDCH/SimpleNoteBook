
LAST_ID = 0

1.create current data format [y m d h m s]
2. f change_id-> += 1

class Note:
    data:str
    title:str
    created_date:str
    id:Callable(change_id)

    f search(filter:str)->bool:
        filter in data | title
    
    f get_id -> int:
    
class Notebook:
    notes:List[Note]

    f new_note(data:str, title:str='')->None:
        global LAST_ID += 1
        notes.append (data, [,title], id)
    
    f searsh_note (id:int, data:str)
    ->str|bool:
        if id in notes
            -> notes
        
    f modify_data()->bool:
        ...
    
    f modify_title()-> bool:
        ...
    
