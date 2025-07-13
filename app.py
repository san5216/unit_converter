import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect
from forms import LengthForm, TemperatureForm, WeightForm


CONVERSION_VALUES = {
    "length": {
        "mm": .001,
        "cm": .01,
        "m": 1,
        "km": 1000,
        "in": .0254,
        "ft": .3048,
        "yd": .9144,
        "mi": 1609.344
    },
    "weight": {
        "mg": .0001,
        "g": .001,
        "kg": 1,
        "oz": 0.02834952,
        "lb": 0.4535924
    }
}


def celcius_to_fahrenheit(degrees_c):
    return (degrees_c * 1.8) + 32


def celcius_to_kelvin(degrees_c):
    return degrees_c + 273.15


def fahrenheit_to_celcius(degrees_f):
    return (degrees_f - 32) / 1.8


def fahrenheit_to_kelvin(degrees_f):
    return ((degrees_f - 32) / 1.8) + 273.15


def kelvin_to_celcius(degrees_k):
    return degrees_k - 273.15


def kelvin_to_fahrenheit(degrees_k):
    return ((degrees_k - 273.15) * 1.8) + 32


def convert_units(value, from_unit, to_unit, unit_type):
    results = {
        "value": value,
        "converted_value": 0.0,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }

    if from_unit == to_unit:
        converted_value = value
    elif from_unit == "c":
        if to_unit == "f":
            converted_value = celcius_to_fahrenheit(value)
        else:
            converted_value = celcius_to_kelvin(value)
    elif from_unit == "f":
        if to_unit == "c":
            converted_value = fahrenheit_to_celcius(value)
        else:
            converted_value = fahrenheit_to_kelvin(value)
    elif from_unit == "k":
        if to_unit == "c":
            converted_value = kelvin_to_celcius(value)
        else:
            converted_value = kelvin_to_fahrenheit(value)
    else:
        from_value = CONVERSION_VALUES[unit_type][from_unit]
        to_value = CONVERSION_VALUES[unit_type][to_unit]

        converted_value = (value * from_value) / to_value

    results["converted_value"] = converted_value

    return results


app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route('/', methods=["GET", "POST"])
@app.route("/length", methods=["GET", "POST"])
def length():
    form = LengthForm()

    if form.validate_on_submit():
        results = convert_units(form.conversion_value.data, form.convert_from.data, form.convert_to.data, "length")
        return render_template("result.html", results=results, btn_redirect="length")
    return render_template("lengths.html", title="Lengths", form=form)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    form = WeightForm()
    if form.validate_on_submit():
        results = convert_units(form.conversion_value.data, form.convert_from.data, form.convert_to.data, "weight")
        return render_template("result.html", results=results, btn_redirect="weight")
    return render_template("weights.html", title="Weights", form=form)


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    form = TemperatureForm()
    if form.validate_on_submit():
        results = convert_units(form.conversion_value.data, form.convert_from.data, form.convert_to.data, "temperature")
        return render_template("result.html", results=results, btn_redirect="temperature")
    return render_template("temperatures.html", title="Temperatures", form=form)


if __name__ == '__main__':
    app.run()
