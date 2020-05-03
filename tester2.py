  
from kivy.app import App
from jnius import autoclass  

PythonActivity=autoclass("org.renpy.android.PythonActivity")
ContactsContract=autoclass("android.provider.ContactsContract")

cr = PythonActivity.mActivity.getContentResolver()
null = None # this will help to convert java examples into python ones :)
cur = cr.query(ContactsContract.Contacts.CONTENT_URI,
            null, null, null, null)
if (cur.getCount() > 0):
    while (cur.moveToNext()):
        id = cur.getString(cur.getColumnIndex(ContactsContract.Contacts._ID));
        name = cur.getString(cur.getColumnIndex(ContactsContract.Contacts.DISPLAY_NAME)) #I think this is not DISPLAY_NAME in all versions ...
        print("->", id, name)