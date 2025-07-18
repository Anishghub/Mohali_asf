# from flask import Flask, render_template, request, jsonify
# import face_recognition
# import numpy as np
# from datetime import datetime
# import cv2
# import os

# app = Flask(__name__)

# # Load known faces
# known_encodings = []
# known_names = []
# for file in os.listdir("known_faces"):
#     img = face_recognition.load_image_file(f"known_faces/{file}")
#     enc = face_recognition.face_encodings(img)
#     if enc:
#         known_encodings.append(enc[0])
#         known_names.append(os.path.splitext(file)[0].upper())

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/mark', methods=['POST'])
# def mark():
#     file = request.files['image']
#     img = face_recognition.load_image_file(file)
#     encodings = face_recognition.face_encodings(img)

#     if not encodings:
#         return jsonify({"status": "fail", "message": "No face detected"})

#     face_encoding = encodings[0]
#     matches = face_recognition.compare_faces(known_encodings, face_encoding)
#     distances = face_recognition.face_distance(known_encodings, face_encoding)

#     if True in matches:
#         index = np.argmin(distances)
#         name = known_names[index]
#         now = datetime.now()
#         with open("attendance.csv", "a") as f:
#             f.write(f"{name},{now.strftime('%d-%m-%Y')},{now.strftime('%I:%M:%S %p')},IN\n")
#         return jsonify({"status": "success", "message": f"{name} marked IN"})
#     else:
#         return jsonify({"status": "fail", "message": "Unknown face"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
 

# IN & OUT 

# from flask import Flask, request, jsonify, render_template
# import face_recognition
# import numpy as np
# from datetime import datetime
# import os

# app = Flask(__name__)

# # Load known faces
# known_encodings = []
# known_names = []
# for file in os.listdir("known_faces"):
#     img = face_recognition.load_image_file(f"known_faces/{file}")
#     enc = face_recognition.face_encodings(img)
#     if enc:
#         known_encodings.append(enc[0])
#         known_names.append(os.path.splitext(file)[0].upper())

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/mark', methods=['POST'])
# def mark_attendance():
#     if 'image' not in request.files or 'status' not in request.form:
#         return jsonify({"status": "fail", "message": "Missing image or status"}), 400

#     file = request.files['image']
#     status = request.form['status']

#     if file.filename == '':
#         return jsonify({"status": "fail", "message": "Empty file"}), 400

#     try:
#         img = face_recognition.load_image_file(file)
#         encodings = face_recognition.face_encodings(img)

#         if not encodings:
#             return jsonify({"status": "fail", "message": "No face detected"}), 200

#         face_encoding = encodings[0]
#         matches = face_recognition.compare_faces(known_encodings, face_encoding)
#         distances = face_recognition.face_distance(known_encodings, face_encoding)

#         if True in matches:
#             index = np.argmin(distances)
#             name = known_names[index]
#             now = datetime.now()
#             date = now.strftime('%d-%m-%Y')
#             time = now.strftime('%I:%M:%S %p')

#             # Ensure CSV file exists
#             if not os.path.exists("attendance.csv"):
#                 with open("attendance.csv", "w") as f:
#                     f.write("Name,Date,Time,Status\n")

#             with open("attendance.csv", "a") as f:
#                 f.write(f"{name},{date},{time},{status}\n")

#             return jsonify({"status": "success", "message": f"{name} marked {status}"}), 200
#         else:
#             return jsonify({"status": "fail", "message": "Unknown face"}), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# IN & OUT 

#  DASHBOARD....START

# from flask import Flask, request, jsonify, render_template, redirect
# import face_recognition
# import numpy as np
# from datetime import datetime
# import os
# import csv

# app = Flask(__name__)

# # Load known faces
# known_encodings = []
# known_names = []
# for file in os.listdir("known_faces"):
#     img = face_recognition.load_image_file(f"known_faces/{file}")
#     enc = face_recognition.face_encodings(img)
#     if enc:
#         known_encodings.append(enc[0])
#         known_names.append(os.path.splitext(file)[0].upper())

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/mark', methods=['POST'])
# def mark_attendance():
#     if 'image' not in request.files or 'status' not in request.form:
#         return jsonify({"status": "fail", "message": "Missing image or status"}), 400

#     file = request.files['image']
#     status = request.form['status']

#     if file.filename == '':
#         return jsonify({"status": "fail", "message": "Empty file"}), 400

#     try:
#         img = face_recognition.load_image_file(file)
#         encodings = face_recognition.face_encodings(img)

#         if not encodings:
#             return jsonify({"status": "fail", "message": "No face detected"}), 200

#         face_encoding = encodings[0]
#         matches = face_recognition.compare_faces(known_encodings, face_encoding)
#         distances = face_recognition.face_distance(known_encodings, face_encoding)

#         if True in matches:
#             index = np.argmin(distances)
#             name = known_names[index]
#             now = datetime.now()
#             date = now.strftime('%d-%m-%Y')
#             time = now.strftime('%I:%M:%S %p')

#             if not os.path.exists("attendance.csv"):
#                 with open("attendance.csv", "w") as f:
#                     f.write("Name,Date,Time,Status\n")

#             with open("attendance.csv", "a") as f:
#                 f.write(f"{name},{date},{time},{status}\n")

#             return jsonify({"status": "success", "message": f"{name} marked {status}"}), 200
#         else:
#             return jsonify({"status": "fail", "message": "Unknown face"}), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# @app.route('/attendance')
# def attendance_dashboard():
#     records = []
#     if os.path.exists("attendance.csv"):
#         with open("attendance.csv", newline='') as f:
#             reader = csv.reader(f)
#             next(reader)  # Skip header
#             for row in reader:
#                 if len(row) == 4:
#                     records.append(row)
#     return render_template("dashboard.html", records=records)

# @app.route('/delete/<int:index>', methods=['POST'])
# def delete_entry(index):
#     rows = []
#     if os.path.exists("attendance.csv"):
#         with open("attendance.csv", newline='') as f:
#             reader = csv.reader(f)
#             header = next(reader)
#             rows = list(reader)
#         if 0 <= index < len(rows):
#             rows.pop(index)
#         with open("attendance.csv", "w", newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(header)
#             writer.writerows(rows)
#     return redirect('/attendance')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

#  DASHBOARD....END


















# Time condition check code here .....

from flask import Flask, request, jsonify, render_template, redirect
import face_recognition
import numpy as np
from datetime import datetime
import os
import csv

app = Flask(__name__)

# Load known faces
known_encodings = []
known_names = []
for file in os.listdir("known_faces"):
    img = face_recognition.load_image_file(f"known_faces/{file}")
    enc = face_recognition.face_encodings(img)
    if enc:
        known_encodings.append(enc[0])
        known_names.append(os.path.splitext(file)[0].upper())

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mark', methods=['POST'])
def mark_attendance():
    """Handle attendance marking allowing **one IN and one OUT per user per day**."""
    if 'image' not in request.files or 'status' not in request.form:
        return jsonify({"status": "fail", "message": "Missing image or status"}), 400

    file = request.files['image']
    status = request.form['status'].upper().strip()  # Ensure status is IN / OUT consistently

    if status not in ("IN", "OUT"):
        return jsonify({"status": "fail", "message": "Invalid status value."}), 400

    if file.filename == '':
        return jsonify({"status": "fail", "message": "Empty file"}), 400

    try:
        img = face_recognition.load_image_file(file)
        encodings = face_recognition.face_encodings(img)

        if not encodings:
            return jsonify({"status": "fail", "message": "NO FACE DETECTED"}), 200

        face_encoding = encodings[0]
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        distances = face_recognition.face_distance(known_encodings, face_encoding)

        if True in matches:
            idx = np.argmin(distances)
            name = known_names[idx]
            now = datetime.now()
            date_str = now.strftime('%d-%m-%Y')
            time_str = now.strftime('%I:%M:%S %p')

            # 🔍 Check if the same user already has the *same status* recorded today
            same_status_already_marked = False
            if os.path.exists("attendance.csv"):
                with open("attendance.csv", newline='') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip header safely
                    for row in reader:
                        if len(row) == 4 and row[0] == name and row[1] == date_str and row[3].upper() == status:
                            same_status_already_marked = True
                            break

            if same_status_already_marked:
                return jsonify({
                    "status": "fail",
                    "message": f"{name}, Attendance successfully marked earlier. {status} today || Have a great day || ({date_str})."
                }), 200

            # ✍️ Append new record (one IN and one OUT per day allowed)
            file_exists = os.path.exists("attendance.csv")
            with open("attendance.csv", "a", newline='') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Name", "Date", "Time", "Status"])
                writer.writerow([name, date_str, time_str, status])

            return jsonify({"status": "success", "message": f"{name} marked {status} successfully."}), 200
        else:
            return jsonify({"status": "fail", "message": "Unknown face"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/attendance')
def attendance_dashboard():
    records = []
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header if present
            for row in reader:
                if len(row) == 4:
                    records.append(row)
    return render_template("dashboard.html", records=records)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_entry(index):
    rows = []
    header = ["Name", "Date", "Time", "Status"]
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", newline='') as f:
            reader = csv.reader(f)
            first = next(reader, None)
            header = first if first and first[0] == "Name" else header
            rows = list(reader) if first else rows
        if 0 <= index < len(rows):
            rows.pop(index)
        with open("attendance.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
    return redirect('/attendance')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# time conditino.... okey code....