from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from model import calculate_grade

app = Flask(__name__)
CORS(app)

@app.route('/add-student', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        name = data.get('name')
        math = float(data.get('math'))
        eng = float(data.get('eng'))
        phy = float(data.get('phy'))
        chem = float(data.get('chem'))
        bio = float(data.get('bio'))
        
        total = math + eng + phy + chem + bio
        avg = round(total / 5, 2)
        grade = calculate_grade(avg)
        
        student = {
            "name": name,
            "math": math,
            "eng": eng,
            "phy": phy,
            "chem": chem,
            "bio": bio,
            "total": total,
            "average": avg,
            "grade": grade
        }
        
        return jsonify({
            "message": "Student added successfully",
            "student": student
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process-class', methods=['POST'])
def process_class():
    try:
        data = request.get_json()
        students = data.get('students', [])
        
        if not students:
            return jsonify({"error": "No students provided"}), 400
        
        processed_students = []
        for s in students:
            math = float(s.get('math'))
            eng = float(s.get('eng'))
            phy = float(s.get('phy'))
            chem = float(s.get('chem'))
            bio = float(s.get('bio'))
            
            total = math + eng + phy + chem + bio
            avg = round(total / 5, 2)
            grade = calculate_grade(avg)
            
            student = {
                "name": s.get('name'),
                "math": math,
                "eng": eng,
                "phy": phy,
                "chem": chem,
                "bio": bio,
                "total": total,
                "average": avg,
                "grade": grade
            }
            processed_students.append(student)
        
        top_student = max(processed_students, key=lambda x: x['average'])
        class_total = sum([s['average'] for s in processed_students])
        class_average = round(class_total / len(processed_students), 2)
        
        return jsonify({
            "students": processed_students,
            "class_summary": {
                "class_average": class_average,
                "top_student": {
                    "name": top_student['name'],
                    "average": top_student['average'],
                    "grade": top_student['grade']
                },
                "total_students": len(processed_students)
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/save-report', methods=['POST'])
def save_report():
    try:
        data = request.get_json()
        students = data.get('students', [])
        class_summary = data.get('class_summary', {})
        filename = data.get('filename', 'student_report.txt')
        
        default_dir = "reports"
        os.makedirs(default_dir, exist_ok=True)
        
        filename = os.path.basename(filename)
        if not filename.lower().endswith('.txt'):
            filename += '.txt'
        
        full_path = os.path.join(default_dir, filename)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("STUDENT RESULT MANAGEMENT SYSTEM REPORT\n\n")
            f.write(f"{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<6}\n")
            f.write("-" * 45 + "\n")
            
            for s in students:
                f.write(f"{s['name']:<15}{s['total']:<10}{s['average']:<10}{s['grade']:<6}\n")
            
            f.write("\n=== CLASS SUMMARY ===\n")
            f.write(f"Class Average: {class_summary.get('class_average', 0)}\n")
            top = class_summary.get('top_student', {})
            f.write(f"Top Student: {top.get('name', 'N/A')} ({top.get('average', 0)}) with Grade {top.get('grade', 'N/A')}\n")
            f.write(f"Total Students: {class_summary.get('total_students', 0)}\n")
        
        return jsonify({
            "message": "Report saved successfully",
            "filepath": full_path
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download-report/<filename>', methods=['GET'])
def download_report(filename):
    try:
        default_dir = "reports"
        filename = os.path.basename(filename)
        full_path = os.path.join(default_dir, filename)
        
        if os.path.exists(full_path):
            return send_file(full_path, as_attachment=True)
        else:
            return jsonify({"error": "File not found"}), 404
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)