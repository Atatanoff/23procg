from sqlalchemy.orm import Session


from data.models import programs, button, macros, icons
from data.database import engine



def save_name_bt(code_bt, name, activity):
    with Session(autoflush=False, bind=engine) as db:
        bt = button.Buttons(buttons=code_bt,
                            name=name,
                            activity=activity)
        db.add(bt)
        db.commit()


        

