from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

UNIT_LABELS = {
    'length': {
        'mm': 'Millimeters (mm)',
        'cm': 'Centimeters (cm)',
        'm': 'Meters (m)',
        'km': 'Kilometers (km)',
        'in': 'Inches (in)',
        'ft': 'Feet (ft)',
        'yd': 'Yards (yd)',
        'mi': 'Miles (mi)'
    },
    "weight": {
        "mg": "Milligrams (mg)",
        "g": "Grams (g)",
        "kg": "Kilograms (kg)",
        "oz": "Ounces (oz)",
        "lb": "Pounds (lb)"
    },
    "temperature": {
        "c": "Celcius",
        "f": "Fahrenheit",
        "k": "Kelvin"
    }
}


def get_unit_choices(unit_type):
    return [(k, UNIT_LABELS[unit_type][k]) for k in UNIT_LABELS[unit_type].keys()]


class LengthForm(FlaskForm):
    conversion_value = FloatField("Enter the length to convert", validators=[DataRequired()])
    convert_from = SelectField("Unit to convert from", validators=[DataRequired()], choices=get_unit_choices("length"))
    convert_to = SelectField("Unit to convert to", validators=[DataRequired()], choices=get_unit_choices("length"))
    submit = SubmitField("Convert")


class WeightForm(FlaskForm):
    conversion_value = FloatField("Enter the weight to convert", validators=[DataRequired()])
    convert_from = SelectField("Unit to convert from", validators=[DataRequired()],
                               choices=get_unit_choices("weight"))
    convert_to = SelectField("Unit to convert to", validators=[DataRequired()], choices=get_unit_choices("weight"))
    submit = SubmitField("Convert")

class TemperatureForm(FlaskForm):
    conversion_value = FloatField("Enter the temperature to convert", validators=[DataRequired()])
    convert_from = SelectField("Unit to convert from", validators=[DataRequired()], choices=get_unit_choices("temperature"))
    convert_to = SelectField("Unit to convert to", validators=[DataRequired()], choices=get_unit_choices("temperature"))
    submit = SubmitField("Convert")
