import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Patient Condition')],
            [sg.InputCombo(('Pain', 'Birth Control', 
                            'Depression', 'High Blood Pressure',
                            'Acne', 'Bipolar Disorde',
                            'Diabetes, Type 2', 'Anxiety',
                            'Insomnia', 'Allergic Rhinitis',
                            'Rheumatoid Arthritis', 'Osteoarthritis',
                            'Migraine', 'Abnormal Uterine Bleeding',
                            'ADHD', 'Major Depressive Disorde',
                            'ibromyalgia', 'Migraine Prevention',
                            'Psoriasis', 'Chronic Pain',
                            'Irritable Bowel Syndrome', 'Endometriosis',
                            'Asthma, Maintenance'), size=(50, 1)),], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Drugs Recommendation', layout)

event, values = window.read()
window.close()

sg.Popup('Drugs Recommendation',
         'The Drugs You can be use is', values)