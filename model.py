from app import db
import datetime

class userstore(db.Model):
    # login password TS
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    password = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    type_of_bed = db.Column(db.String(64))
    date_of_admission = db.Column(db.Date, default=datetime.date.today().strftime("%Y-%m-%d"))
    date_of_discharge = db.Column(db.Date)
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    status = db.Column(db.String(64))
    number_of_days = db.Column(db.Integer)


class MedicineMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(64), index=True)
    quantity = db.Column(db.Integer)
    rate = db.Column(db.Integer)

class Medicines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicineID = db.Column(db.Integer, db.ForeignKey('medicinemaster.id'), nullable=False)
    quantity = db.Column(db.Integer)
    patientID = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)


class DiagnosticMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    test_name = db.Column(db.String(64), index=True)
    test_charge = db.Column(db.Integer)

class Diagnostics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientID = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    testID = db.Column(db.Integer, db.ForeignKey('diagnosticmaster.id'), nullable=False)



