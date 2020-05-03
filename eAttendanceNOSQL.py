eAttendance = {
  'codes':{
    # code_id, l_code, c_status, c_user, code
  },
  'Countries': {# open list for Coconut
      'Nigeria':{
          'region':'West Africa',
          'Universities':{
              'Federal University Gusau':{
                  'abbr':'FUG',
                  'address':'Zaria Road Gusau',
                  }
            },
          'polytechnics':{
            "Abdu Gusau Polytechnic":{
              "abbr":"AGP",
              'address': "Talata Mafara"
            }

          },
          'colleges of Education':{
            'College of Education Maru':{
              'abbr': 'COEM',
              'address':'Maru'
            }

          }
      }
  },

  'lecture':{
    #   l_code, no_in_attendance, lecture_no, no_signed_up, taking_id, lecture_id, date_taken, accessor
  },
  'lecturer':{
        'aminumuhd@gmail.com':
        {'title':'Prof.', 'l_name':'Aminu Muhammad', 'password':'1234gummi', 'phone':'08167768410'}
  },
  'lecturing':{
    #   lecturing_id
    'Nigeria-Federal University Gusau-aminumuhd@gmail.com':{
        'lecture numbers-CSC407' : 0,
        '12122':{
            'course code':'CSC407',
            'accessKey':'321ewq',
            'title':'Computer Networks',
            'unit': 3,
            'session': '2019/2020'
        }
    }
  },
  
  'programmes':{# open list for Coconut
    '1': 'Computer Science'
  },
  'register':{
    'Ng-FUG-aminumuhd@gmail.com-CSC407-usoofali@gmail.com':{
        'attendance':0,
        'CA': 0,
        'Exam':0,
        'CSC407':{
            'title':'Computer Networks',
            'unit': 3,
            'session': '2019/2020'
        }
  },
  
  'student':{
      'Ng-FUG-usoofali@gmail.com':{
        'adm_no':'1610308027',
        's_name': 'Aliyu Yusuf', 
        'programme':'Computer Science', 
        'university':'Ng-FUG',
        'student_id':'NGFUG1610308027', 
        'level': '400L'
      }
      
  },
  
      
  }

}